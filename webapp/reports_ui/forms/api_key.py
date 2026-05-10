from django import forms


class ApiKeyForm(forms.Form):
    api_key = forms.CharField(
        label="API ключ",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите API ключ'
        }),
        required=True,
        help_text="Введите ваш API ключ для доступа к данным"
    )