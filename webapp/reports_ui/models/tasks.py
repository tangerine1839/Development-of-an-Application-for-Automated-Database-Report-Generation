from django.db import models


class ReportTaskParams(models.Model):
    title = models.CharField(max_length=200, default="Отчёт по задачам")
    status = models.JSONField(default=list)
    created_at_from = models.DateTimeField(null=True, blank=True)
    created_at_to = models.DateTimeField(null=True, blank=True)
    finished_at_from = models.DateTimeField(null=True, blank=True)
    finished_at_to = models.DateTimeField(null=True, blank=True)
    columns = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title