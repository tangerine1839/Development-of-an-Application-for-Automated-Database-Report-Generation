from django import forms
from datetime import date, timedelta


class ReportUsersInspectionsCountForm(forms.Form):
    SORTING_CHOICES = [
        ('desc', 'По убыванию (сначала больше)'),
        ('asc', 'По возрастанию (сначала меньше)'),
    ]

    date_from = forms.DateField(
        label="Дата начала",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    date_to = forms.DateField(
        label="Дата окончания",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    sorting = forms.ChoiceField(
        label="Сортировка",
        choices=SORTING_CHOICES,
        widget=forms.RadioSelect,
        initial='desc',
        required=True,
    )

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')

        if date_from and date_to and date_from > date_to:
            raise forms.ValidationError("Дата начала не может быть позже даты окончания")

        return cleaned_data