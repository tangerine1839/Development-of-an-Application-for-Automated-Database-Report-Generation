from django import forms

from main.reports.inspection_items import INSPECTION_ITEM_FIELDS


class ReportItemsForm(forms.Form):
    inspection_id = forms.IntegerField(
        label="ID проверки",
        required=True,
    )

    EXTRA_FIELD_CHOICES = [(f.name, f.label) for f in INSPECTION_ITEM_FIELDS]
    extra_fields = forms.MultipleChoiceField(
        label="Дополнительные поля для Excel",
        choices=EXTRA_FIELD_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )