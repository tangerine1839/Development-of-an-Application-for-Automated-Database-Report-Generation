# webapp/reports_ui/forms/inspections.py
from django import forms

from main.api_client.filters.inspection_filters import InspectionFilterSet, TimeRange, Status
from main.reports.inspections_excel import INSPECTION_FIELDS


STATUS_CHOICES = [
    ("created", "Создано"),
    ("completed", "Завершено"),
    ("process", "В процессе"),
    ("verification", "На проверке"),
]


class ReportInspectionForm(forms.Form):
    status = forms.MultipleChoiceField(
        label="Статус проверки",
        choices=STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    date_from = forms.DateTimeField(
        label="Дата проверки (от)",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )
    date_to = forms.DateTimeField(
        label="Дата проверки (до)",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )

    place_ids = forms.CharField(
        label="ID объектов (через запятую)",
        required=False,
        help_text="Пример: 123, 456",
        widget=forms.TextInput(attrs={"placeholder": "123, 456, ..."}),
    )

    creator_ids = forms.CharField(
        label="ID создателей (через запятую)",
        required=False,
        help_text="Пример: 475785, 585962",
        widget=forms.TextInput(attrs={"placeholder": "475785, 585962, ..."}),
    )

    assignee_ids = forms.CharField(
        label="ID исполнителей (через запятую)",
        required=False,
        help_text="Пример: 859594, 987654",
        widget=forms.TextInput(attrs={"placeholder": "859594, 987654, ..."}),
    )

    is_guest = forms.BooleanField(
        label="Только гостевые проверки",
        required=False,
        help_text="Если отмечено, будут показаны только гостевые инспекции.",
    )

    FIELD_CHOICES = [(f.name, f.label) for f in INSPECTION_FIELDS]

    excel_fields = forms.MultipleChoiceField(
        label="Поля для Excel",
        choices=FIELD_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Выберите один или несколько столбцов",
    )