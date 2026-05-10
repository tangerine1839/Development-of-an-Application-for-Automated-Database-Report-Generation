# webapp/reports_ui/views/task_messages.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from io import BytesIO

from httpx import HTTPStatusError

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.config import settings
from main.reports.inspection_items import create_inspection_items_excel
from webapp.reports_ui.forms.inspection_items import ReportItemsForm


def report_inspection_items_form(request):
    error_message = None
    api_key = request.session.get('api_key')
    if not api_key:
        messages.warning(request, "Пожалуйста, введите API ключ для доступа к отчетам")
        return redirect('reports_ui:main_page')
    if request.method == "POST":
        form = ReportItemsForm(request.POST)
        if form.is_valid():
            inspection_id = form.cleaned_data.get("inspection_id")
            extra_fields = form.cleaned_data.get("extra_fields", [])

            try:
                with CheckOfficeAPIClient(
                        api_key=api_key,
                        base_url=settings.CHECK_OFFICE_BASE_URL,
                ) as client:
                    response = client.get_inspection_by_id(inspection_id)

                    inspection = response.data

            except HTTPStatusError as e:
                if e.response.status_code == 404:
                    error_message = f"Проверка с ID {inspection_id} не найдена."
                else:
                    error_message = f"Ошибка при получении проверки: {str(e)}"
                return render(
                    request,
                    "reports_ui/report_inspection_items_form.html",
                    {"form": form, "error_message": error_message},
                )

            wb = create_inspection_items_excel(
                inspection =inspection,
                include_columns=extra_fields if extra_fields else None,
            )

            virtual_workbook = BytesIO()
            wb.save(virtual_workbook)
            virtual_workbook.seek(0)

            response = HttpResponse(
                virtual_workbook.getvalue(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = 'attachment; filename="report_inspection_items.xlsx"'
            return response

        return render(
            request,
            "reports_ui/report_inspection_items_form.html",
            {"form": form, "error_message": error_message},
        )

    else:
        form = ReportItemsForm()

    return render(
        request,
        "reports_ui/report_inspection_items_form.html",
        {"form": form, "error_message": error_message},
    )