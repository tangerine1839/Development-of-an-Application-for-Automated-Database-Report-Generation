# reports_ui/views/index.py
from django.shortcuts import render

def index(request):
    reports = [
        ("tasks", "Отчёт по списку задач"),
        ("objects", "Отчёт по объектам"),
        ("inspections", "Отчет по проверкам"),
        ("task_messages", "Отчет по сообщениям задачи"),
        ("inspection_items", "Отчет по пунктам проверки"),
        ("users", "Отчет по списку пользователей")
    ]
    return render(request, "reports_ui/index.html", {"reports": reports})