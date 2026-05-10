from django import forms

from main.reports.task_messages_excel import MESSAGE_FIELDS


class ReportMessagesForm(forms.Form):
    task_id = forms.IntegerField(
        label="ID задачи",
        required=True,
    )

    EXTRA_FIELD_CHOICES = [(f.name, f.label) for f in MESSAGE_FIELDS]
    extra_fields = forms.MultipleChoiceField(
        label="Дополнительные поля для Excel",
        choices=EXTRA_FIELD_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )