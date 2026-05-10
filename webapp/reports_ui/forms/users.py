from django import forms

from main.reports.users_excel import USER_FIELDS


class ReportUserForm(forms.Form):

    ids = forms.CharField(
        label="ID пользователей (через запятую)",
        required=False,
        widget=forms.TextInput(),
    )

    permission_group = forms.CharField(
        label="Группы прав (через запятую)",
        required=False,
        widget=forms.TextInput(),
    )


    FIELD_CHOICES = [(f.name, f.label) for f in USER_FIELDS]

    excel_fields = forms.MultipleChoiceField(
        label="Поля для Excel",
        choices=FIELD_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Выберите один или несколько столбцов",
    )