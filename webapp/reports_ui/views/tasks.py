from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from io import BytesIO
from django.contrib import messages


from django.utils import timezone

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.api_client.filters.task_filters import TaskFilterSet, TimeRange
from main.config import settings
from main.reports.tasks_excel import create_tasks_excel
from webapp.reports_ui.forms import ReportTaskForm



def report_task_form(request):
    error_message = None
    api_key = request.session.get('api_key')
    if not api_key:
        messages.warning(request, "Пожалуйста, введите API ключ для доступа к отчетам")
        return redirect('reports_ui:main_page')
    if request.method == "POST":
        form = ReportTaskForm(request.POST)
        if form.is_valid():
            status_raw = form.cleaned_data.get("status", [])
            status = list(status_raw) if status_raw else None

            created_at_from = form.cleaned_data.get("created_at_from")
            created_at_to = form.cleaned_data.get("created_at_to")

            finished_at_from = form.cleaned_data.get("finished_at_from")
            finished_at_to = form.cleaned_data.get("finished_at_to")
            creator_id_raw = form.cleaned_data.get("creator_id")
            assignee_id_raw = form.cleaned_data.get("assignee_id")
            excel_fields = form.cleaned_data.get("excel_fields", [])


            creator_id = [s.strip() for s in creator_id_raw.split(",") if s.strip()] if creator_id_raw else None
            assignee_id = [s.strip() for s in assignee_id_raw.split(",") if s.strip()] if assignee_id_raw else None

            filters = TaskFilterSet(
                status=status,
                created_at=TimeRange(from_=created_at_from, to=created_at_to),
                finished_at=TimeRange(from_=finished_at_from, to=finished_at_to),
                creator_id=creator_id,
                assignee_id=assignee_id,

            )

            with CheckOfficeAPIClient(
                api_key=api_key,
                base_url=settings.CHECK_OFFICE_BASE_URL,
            ) as client:
                resp = client.get_tasks(page=1, per_page=30, filters=filters)

                # Проверяем, есть ли вообще задачи
                if resp.total == 0:
                    error_message = "По выбранным фильтрам не найдено ни одной задачи."

                    return render(
                        request,
                        "reports_ui/report_task_form.html",
                        {"form": form, "error_message": error_message}
                    )
                tasks = client.get_all_tasks(filters=filters)
                filtered = filters.filter_python(tasks)


            wb = create_tasks_excel(
                tasks=filtered,
                columns=excel_fields,
            )

            virtual_workbook = BytesIO()
            wb.save(virtual_workbook)
            virtual_workbook.seek(0)

            response = HttpResponse(
                virtual_workbook.getvalue(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = 'attachment; filename="report_tasks.xlsx"'
            return response

        return render(request, "reports_ui/report_task_form.html", {"form": form})
    else:
        form = ReportTaskForm()


    return render(request, "reports_ui/report_task_form.html", {"form": form, "error_message": error_message})