from django import forms
from datetime import date, timedelta


class ReportInspectionsCountForm(forms.Form):
    GROUPING_CHOICES = [
        ('day', 'По дням'),
        ('month', 'По месяцам'),
    ]

    grouping = forms.ChoiceField(
        label="Группировка",
        choices=GROUPING_CHOICES,
        widget=forms.RadioSelect,
        initial='day',
        required=True,
    )

    date_from = forms.DateField(
        label="Дата начала",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today() - timedelta(days=30),
    )

    date_to = forms.DateField(
        label="Дата окончания",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today(),
    )

    EXPORT_FORMAT_CHOICES = [
        ('excel', 'Excel файл'),
        ('chart', 'Столбчатый график'),
    ]

    export_format = forms.ChoiceField(
        label="Формат отчёта",
        choices=EXPORT_FORMAT_CHOICES,
        widget=forms.RadioSelect,
        initial='excel',
        required=True,
    )

