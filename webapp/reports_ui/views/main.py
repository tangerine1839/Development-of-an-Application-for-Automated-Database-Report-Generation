from django.shortcuts import render, redirect
from django.contrib import messages
from httpx import HTTPStatusError

from main.api_client.check_office_client import CheckOfficeAPIClient
from main.config import settings
from webapp.reports_ui.forms.api_key import ApiKeyForm


def main_page(request):
    """Страница ввода API ключа"""

    # Если уже есть ключ в сессии, перенаправляем на страницу с отчетами
    if 'api_key' in request.session:
        return redirect('reports_ui:index')

    if request.method == "POST":
        form = ApiKeyForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']

            # Проверяем API ключ
            try:
                with CheckOfficeAPIClient(
                        api_key=api_key,
                        base_url=settings.CHECK_OFFICE_BASE_URL,
                ) as client:
                    # Делаем простой запрос для проверки ключа
                    client.get_users(page=1, per_page=1)

                    # Если успешно - сохраняем ключ в сессии
                    request.session['api_key'] = api_key
                    messages.success(request, "API ключ успешно подключен")
                    return redirect('reports_ui:index')

            except HTTPStatusError as e:
                if e.response.status_code == 401:
                    messages.error(request, "Неверный API ключ. Пожалуйста, проверьте и попробуйте снова.")
                else:
                    messages.error(request, f"Ошибка подключения: {str(e)}")
            except Exception as e:
                messages.error(request, f"Ошибка подключения: {str(e)}")

            return render(request, "reports_ui/main_page.html", {"form": form})
    else:
        form = ApiKeyForm()

    return render(request, "reports_ui/main_page.html", {"form": form})


def logout_api(request):
    """Выход - удаление API ключа из сессии"""
    if 'api_key' in request.session:
        del request.session['api_key']
        messages.info(request, "Вы отключились от API")
    return redirect('reports_ui:main_page')