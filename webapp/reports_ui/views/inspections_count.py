from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from io import BytesIO
from datetime import datetime, date, timedelta

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.api_client.filters.inspection_filters import InspectionFilterSet, TimeRange
from main.config import settings
from main.reports.inspections_count_excel import create_inspections_count_excel
from main.reports.inspections_count_chart import create_inspections_count_chart
from webapp.reports_ui.forms.inspections_count import ReportInspectionsCountForm


def get_periods_list(date_from: date, date_to: date, grouping: str) -> list:
    periods = []
    current = date_from

    if grouping == 'day':
        while current <= date_to:
            periods.append(current)
            current += timedelta(days=1)
    else:
        while current <= date_to:
            periods.append(current)
            if current.month == 12:
                current = current.replace(year=current.year + 1, month=1)
            else:
                current = current.replace(month=current.month + 1)

    return periods


def get_period_end_date(period_start: date, grouping: str) -> date:
    if grouping == 'day':
        return period_start
    else:
        next_month = period_start.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)


def get_inspections_count_for_period(
        client: CheckOfficeAPIClient,
        period_start: date,
        period_end: date,
) -> int:


    start_datetime = datetime.combine(period_start, datetime.min.time())
    end_datetime = datetime.combine(period_end, datetime.max.time())

    filters = InspectionFilterSet(
        date=TimeRange(
            from_=start_datetime,
            to=end_datetime,
        )
    )

    response = client.get_inspections(page=1, per_page=1, filters=filters)
    return response.total


def report_inspections_count_form(request):
    error_message = None
    api_key = request.session.get('api_key')
    if not api_key:
        messages.warning(request, "Пожалуйста, введите API ключ для доступа к отчетам")
        return redirect('reports_ui:main_page')
    if request.method == "POST":
        form = ReportInspectionsCountForm(request.POST)

        if form.is_valid():
            grouping = form.cleaned_data.get("grouping")
            date_from = form.cleaned_data.get("date_from")
            date_to = form.cleaned_data.get("date_to")
            export_format = form.cleaned_data.get("export_format")

            if not date_from or not date_to or date_from > date_to:
                error_message = "Необходимо выбрать дату начала и дату окончания. Дата начала должна быть меньше даты окончания."
                return render(
                    request,
                    "reports_ui/report_inspections_count_form.html",
                    {"form": form, "error_message": error_message},
                )

            periods = get_periods_list(date_from, date_to, grouping)

            try:
                with CheckOfficeAPIClient(
                        api_key=api_key,
                        base_url=settings.CHECK_OFFICE_BASE_URL,
                ) as client:

                    data = []
                    for period_start in periods:
                        period_end = get_period_end_date(period_start, grouping)
                        count = get_inspections_count_for_period(client, period_start, period_end)

                        data.append({
                            'period': period_start,
                            'count': count,
                        })

                    if export_format == 'excel':
                        wb = create_inspections_count_excel(
                            data=data,
                            grouping=grouping,
                            date_from=date_from,
                            date_to=date_to,
                            heading="Отчёт по количеству проверок",
                        )

                        virtual_workbook = BytesIO()
                        wb.save(virtual_workbook)
                        virtual_workbook.seek(0)

                        response = HttpResponse(
                            virtual_workbook.getvalue(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        )
                        filename = f"inspections_count_{date_from.strftime('%Y%m%d')}_{date_to.strftime('%Y%m%d')}.xlsx"
                        response["Content-Disposition"] = f'attachment; filename="{filename}"'
                        return response

                    else:
                        chart_image = create_inspections_count_chart(
                            data=data,
                            grouping=grouping,
                            date_from=date_from,
                            date_to=date_to,
                        )

                        import base64
                        image_data = base64.b64decode(chart_image)

                        response = HttpResponse(
                            image_data,
                            content_type="image/png",
                        )
                        filename = f"inspections_count_{date_from.strftime('%Y%m%d')}_{date_to.strftime('%Y%m%d')}.png"
                        response["Content-Disposition"] = f'attachment; filename="{filename}"'
                        return response

            except Exception as e:
                error_message = f"Ошибка при получении данных: {str(e)}"
                return render(
                    request,
                    "reports_ui/report_inspections_count_form.html",
                    {"form": form, "error_message": error_message},
                )

        return render(
            request,
            "reports_ui/report_inspections_count_form.html",
            {"form": form, "error_message": error_message},
        )

    else:
        form = ReportInspectionsCountForm()

    return render(
        request,
        "reports_ui/report_inspections_count_form.html",
        {"form": form, "error_message": error_message},
    )