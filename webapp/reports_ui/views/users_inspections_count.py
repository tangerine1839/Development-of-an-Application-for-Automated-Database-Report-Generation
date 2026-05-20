from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from io import BytesIO
from datetime import datetime, date, timedelta

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.api_client.filters.inspection_filters import InspectionFilterSet, TimeRange
from main.api_client.filters.user_filters import UserFilterSet
from main.config import settings
from main.reports.users_inspections_count_excel import create_users_inspections_count_excel
from webapp.reports_ui.forms.user_inspections_count import ReportUsersInspectionsCountForm


def get_user_inspections_count(
        client: CheckOfficeAPIClient,
        user_id: int,
        date_from: datetime,
        date_to: datetime,
) -> int:

    filters = InspectionFilterSet(
        assignee_ids=[user_id],
        date=TimeRange(
            from_=date_from,
            to=date_to,
        )
    )

    response = client.get_inspections(page=1, per_page=1, filters=filters)
    return response.total


def report_users_inspections_count_form(request):
    error_message = None
    api_key = request.session.get('api_key')

    if not api_key:
        messages.warning(request, "Пожалуйста, введите API ключ для доступа к отчетам")
        return redirect('reports_ui:main_page')

    if request.method == "POST":
        form = ReportUsersInspectionsCountForm(request.POST)

        if form.is_valid():
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
            sorting = form.cleaned_data['sorting']

            # Проверка на корректные даты
            if date_from > date_to:
                error_message = "Дата начала не может быть позже даты окончания"
                return render(
                    request,
                    "reports_ui/report_users_inspections_count_form.html",
                    {"form": form, "error_message": error_message},
                )

            start_datetime = datetime.combine(date_from, datetime.min.time())
            end_datetime = datetime.combine(date_to, datetime.max.time())

            try:
                with CheckOfficeAPIClient(
                        api_key=api_key,
                        base_url=settings.CHECK_OFFICE_BASE_URL,
                ) as client:

                    # Получаем всех пользователей
                    users = client.get_all_users(filters=UserFilterSet())

                    if not users:
                        error_message = "Не найдено ни одного пользователя."
                        return render(
                            request,
                            "reports_ui/report_users_inspections_count_form.html",
                            {"form": form, "error_message": error_message},
                        )

                    # Для каждого пользователя получаем количество проверок
                    data = []
                    for user in users:
                        count = get_user_inspections_count(
                            client,
                            user.id,
                            start_datetime,
                            end_datetime
                        )

                        data.append({
                            'user_id': user.id,
                            'user_name': user.name,
                            'position': user.position or "",
                            'inspections_count': count,
                        })

                    reverse_sort = (sorting == 'desc')
                    data.sort(key=lambda x: x['inspections_count'], reverse=reverse_sort)

                    wb = create_users_inspections_count_excel(
                        data=data,
                        date_from=date_from,
                        date_to=date_to,
                        sorting=sorting,
                        heading="Отчёт по количеству проверок у пользователей",
                    )

                    virtual_workbook = BytesIO()
                    wb.save(virtual_workbook)
                    virtual_workbook.seek(0)

                    response = HttpResponse(
                        virtual_workbook.getvalue(),
                        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )
                    filename = f"users_inspections_count_{date_from.strftime('%Y%m%d')}_{date_to.strftime('%Y%m%d')}.xlsx"
                    response["Content-Disposition"] = f'attachment; filename="{filename}"'
                    return response

            except Exception as e:
                error_message = f"Ошибка при получении данных: {str(e)}"
                return render(
                    request,
                    "reports_ui/report_users_inspections_count_form.html",
                    {"form": form, "error_message": error_message},
                )

        # Если форма не валидна
        else:
            if form.non_field_errors():
                error_message = form.non_field_errors()[0]
            elif form.errors:
                errors_list = []
                for field, errors in form.errors.items():
                    field_label = form.fields[field].label
                    errors_list.append(f"{field_label}: {', '.join(errors)}")
                error_message = "; ".join(errors_list)

            return render(
                request,
                "reports_ui/report_users_inspections_count_form.html",
                {"form": form, "error_message": error_message},
            )

    else:
        initial_data = {
            'date_from': date.today() - timedelta(days=30),
            'date_to': date.today(),
        }
        form = ReportUsersInspectionsCountForm(initial=initial_data)

    return render(
        request,
        "reports_ui/report_users_inspections_count_form.html",
        {"form": form, "error_message": error_message},
    )