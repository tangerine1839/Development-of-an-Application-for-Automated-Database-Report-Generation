# webapp/reports_ui/views/objects.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from io import BytesIO
from django.contrib import messages

from django.utils import timezone

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.api_client.filters.object_filters import ObjectFilterSet
from main.config import settings
from main.reports.objects_excel import create_objects_excel
from webapp.reports_ui.forms import ReportObjectForm


def report_object_form(request):
    error_message = None
    api_key = request.session.get('api_key')
    if not api_key:
        messages.warning(request, "Пожалуйста, введите API ключ для доступа к отчетам")
        return redirect('reports_ui:main_page')
    if request.method == "POST":
        form = ReportObjectForm(request.POST)
        if form.is_valid():
            codes_raw = form.cleaned_data.get("codes", "")
            manager_raw = form.cleaned_data.get("manager", "")
            codes = [s.strip() for s in codes_raw.split(",") if s.strip()] if codes_raw else None
            manager = [s.strip() for s in manager_raw.split(",") if s.strip()] if codes_raw else None
            excel_fields = form.cleaned_data.get("excel_fields", [])

            filters = ObjectFilterSet(
                codes=codes,
                manager=manager,
            )

            with CheckOfficeAPIClient(
                api_key=api_key,
                base_url=settings.CHECK_OFFICE_BASE_URL,
            ) as client:
                resp = client.get_objects(page=1, per_page=30, filters=filters)

                if resp.data.total == 0:
                    error_message = (
                        "По выбранным фильтрам не найдено ни одного объекта."
                    )
                    return render(
                        request,
                        "reports_ui/report_object_form.html",
                        {"form": form, "error_message": error_message},
                    )

                objects = client.get_all_objects(filters=filters)
            filtered = filters.filter_python(objects)
            wb = create_objects_excel(
                objects=filtered,
                columns=excel_fields,
            )

            virtual_workbook = BytesIO()
            wb.save(virtual_workbook)
            virtual_workbook.seek(0)

            response = HttpResponse(
                virtual_workbook.getvalue(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = 'attachment; filename="report_objects.xlsx"'
            return response

        # если форма не валидна
        return render(
            request,
            "reports_ui/report_object_form.html",
            {"form": form, "error_message": error_message},
        )

    else:
        form = ReportObjectForm()

    return render(
        request,
        "reports_ui/report_object_form.html",
        {"form": form, "error_message": error_message},
    )