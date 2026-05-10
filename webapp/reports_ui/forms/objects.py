from django import forms

from main.reports.objects_excel import OBJECT_FIELDS


class ReportObjectForm(forms.Form):
    codes = forms.CharField(
        label="Коды объектов (через запятую)",
        required=False,
        help_text="Пример: Дороги, Парки",
        widget=forms.TextInput(attrs={"placeholder": "Дороги, Парки, ..."}),
    )
    manager = forms.CharField(
        label="Менеджеры (через запятую)",
        required=False,
        widget=forms.TextInput(),
    )
    FIELD_CHOICES = [(f.name, f.label) for f in OBJECT_FIELDS]
    excel_fields = forms.MultipleChoiceField(
        label="Поля для Excel",
        choices=FIELD_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Выберите один или несколько столбцов",
    )