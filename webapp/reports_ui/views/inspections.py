# webapp/reports_ui/views/inspections.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from io import BytesIO
from django.contrib import messages

from django.utils import timezone

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.api_client.filters.inspection_filters import InspectionFilterSet, TimeRange
from main.config import settings
from main.reports.inspections_excel import create_inspections_excel
from webapp.reports_ui.forms.inspections import ReportInspectionForm


def report_inspection_form(request):
    error_message = None
    api_key = request.session.get('api_key')
    if not api_key:
        messages.warning(request, "Пожалуйста, введите API ключ для доступа к отчетам")
        return redirect('reports_ui:main_page')
    if request.method == "POST":
        form = ReportInspectionForm(request.POST)
        if form.is_valid():
            status_raw = form.cleaned_data.get("status", [])
            status = list(status_raw) if status_raw else None

            date_from = form.cleaned_data.get("date_from")
            date_to = form.cleaned_data.get("date_to")

            place_ids_raw = form.cleaned_data.get("place_ids", "")
            place_ids = (
                [int(s.strip()) for s in place_ids_raw.split(",") if s.strip()]
                if place_ids_raw else None
            )

            creator_ids_raw = form.cleaned_data.get("creator_ids", "")
            creator_ids = (
                [int(s.strip()) for s in creator_ids_raw.split(",") if s.strip()]
                if creator_ids_raw else None
            )

            assignee_ids_raw = form.cleaned_data.get("assignee_ids", "")
            assignee_ids = (
                [int(s.strip()) for s in assignee_ids_raw.split(",") if s.strip()]
                if assignee_ids_raw else None
            )

            is_guest = form.cleaned_data.get("is_guest", None)

            excel_fields = form.cleaned_data.get("excel_fields", [])

            filters = InspectionFilterSet(
                status=status,
                date=TimeRange(from_=date_from, to=date_to),
                place_ids=place_ids,
                creator_ids=creator_ids,
                assignee_ids=assignee_ids,
                is_guest=is_guest,
            )

            with CheckOfficeAPIClient(
                api_key=api_key,
                base_url=settings.CHECK_OFFICE_BASE_URL,
            ) as client:
                resp = client.get_inspections(page=1, per_page=30, filters=filters)

                if resp.total == 0:
                    error_message = "По выбранным фильтрам не найдено ни одной инспекции."
                    return render(
                        request,
                        "reports_ui/report_inspection_form.html",
                        {"form": form, "error_message": error_message},
                    )

                inspections = client.get_all_inspections(filters=filters)
                filtered = filters.filter_python(inspections)

            wb = create_inspections_excel(
                inspections=filtered,
                columns=excel_fields,
                heading="Отчёт по инспекциям",
            )

            virtual_workbook = BytesIO()
            wb.save(virtual_workbook)
            virtual_workbook.seek(0)

            response = HttpResponse(
                virtual_workbook.getvalue(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = 'attachment; filename="report_inspections.xlsx"'
            return response

        return render(
            request,
            "reports_ui/report_inspection_form.html",
            {"form": form, "error_message": error_message},
        )

    else:
        form = ReportInspectionForm()

    return render(
        request,
        "reports_ui/report_inspection_form.html",
        {"form": form, "error_message": error_message},
    )