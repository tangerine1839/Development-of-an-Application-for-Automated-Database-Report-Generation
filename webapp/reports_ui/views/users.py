from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from io import BytesIO
from django.contrib import messages


from django.utils import timezone

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.api_client.filters.user_filters import UserFilterSet
from main.config import settings
from main.reports.users_excel import create_users_excel
from webapp.reports_ui.forms import ReportTaskForm, ReportUserForm


def report_user_form(request):
    error_message = None
    api_key = request.session.get('api_key')
    if not api_key:
        messages.warning(request, "Пожалуйста, введите API ключ для доступа к отчетам")
        return redirect('reports_ui:main_page')
    if request.method == "POST":
        form = ReportUserForm(request.POST)
        if form.is_valid():

            ids_ = form.cleaned_data.get("ids")
            permission_group_ = form.cleaned_data.get("permission_group")
            excel_fields = form.cleaned_data.get("excel_fields", [])


            ids = [s.strip() for s in ids_.split(",") if s.strip()] if ids_ else None
            permission_group = [s.strip() for s in permission_group_.split(",") if s.strip()] if permission_group_ else None

            filters = UserFilterSet(
                ids=ids,
                permission_groups=permission_group,
            )

            with CheckOfficeAPIClient(
                api_key=api_key,
                base_url=settings.CHECK_OFFICE_BASE_URL,

            ) as client:
                resp = client.get_users(page=1, per_page=30, filters=filters)

                if resp.total == 0:
                    error_message = "По выбранным фильтрам не найдено ни одного пользователя."

                    return render(
                        request,
                        "reports_ui/report_user_form.html",
                        {"form": form, "error_message": error_message}
                    )
                users = client.get_all_users(filters=filters)


            wb = create_users_excel(
                users=users,
                include_columns=excel_fields,
            )

            virtual_workbook = BytesIO()
            wb.save(virtual_workbook)
            virtual_workbook.seek(0)

            response = HttpResponse(
                virtual_workbook.getvalue(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = 'attachment; filename="report_users.xlsx"'
            return response

        return render(request, "reports_ui/report_user_form.html", {"form": form})
    else:
        form = ReportUserForm()


    return render(request, "reports_ui/report_user_form.html", {"form": form, "error_message": error_message})