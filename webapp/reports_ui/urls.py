from django.urls import path
from .views import index, report_task_form, report_object_form, report_inspection_form, report_task_messages_form, \
    report_inspection_items_form, report_user_form
from .views.inspections_count import report_inspections_count_form
from .views.main import main_page, logout_api
from .views.users_inspections_count import report_users_inspections_count_form

app_name = "reports_ui"

urlpatterns = [
    #path("", index, name="index"),
    path("", main_page, name="main_page"),

    # Страница с выбором отчетов
    path("reports/", index, name="index"),

    # Выход из API
    path("logout/", logout_api, name="logout_api"),
    path("tasks/", report_task_form, name="report_task"),
    path("objects/", report_object_form, name="report_object"),
    path("inspections/", report_inspection_form, name="report_inspection"),
    path("task_messages/", report_task_messages_form, name="report_task_messages"),
    path("inspection_items/", report_inspection_items_form, name="report_inspection_items"),
    path("users/", report_user_form, name="report_user"),
    path('inspections_count/', report_inspections_count_form, name='inspections_count_form'),
path('users_inspections_count/', report_users_inspections_count_form, name='users_inspections_count_form'),
]