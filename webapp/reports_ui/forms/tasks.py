from django import forms

from main.api_client.filters.task_filters import TaskFilterSet, TimeRange, Status
from main.reports.tasks_excel import TASK_FIELDS

STATUS_CHOICES = [
    ("completed", "Завершено"),
    ("created", "Создано"),
    ("process", "В процессе"),
    ("revise", "На доработке"),
    ("review", "На проверке"),
    ("validation", "Валидация"),
    ("archived", "Архив"),
    ("manual_review", "Ручная проверка"),
    ("cancelled", "Отменено"),
]


class ReportTaskForm(forms.Form):
    status = forms.MultipleChoiceField(
        label="Статус задачи",
        choices=STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    creator_id = forms.CharField(
        label="ID создателя (через запятую)",
        required=False,
        widget=forms.TextInput(),
    )

    assignee_id = forms.CharField(
        label="ID исполнителя (через запятую)",
        required=False,
        widget=forms.TextInput(),
    )

    created_at_from = forms.DateTimeField(
        label="Создано в (от)",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )
    created_at_to = forms.DateTimeField(
        label="Создано в (до)",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )

    finished_at_from = forms.DateTimeField(
        label="Завершено в (от)",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )
    finished_at_to = forms.DateTimeField(
        label="Завершено в (до)",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )

    FIELD_CHOICES = [(f.name, f.label) for f in TASK_FIELDS]

    excel_fields = forms.MultipleChoiceField(
        label="Поля для Excel",
        choices=FIELD_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Выберите один или несколько столбцов",
    )