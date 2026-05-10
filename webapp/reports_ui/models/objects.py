# webapp/reports_ui/models/objects.py
from django.db import models


class ReportObjectParams(models.Model):
    title = models.CharField(
        max_length=200,
        default="Отчёт по объектам",
    )
    codes = models.JSONField(
        default=list,
        help_text="Список кодов объектов"
    )
    columns = models.JSONField(
        default=list,
        help_text="Выбранные поля для Excel"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title