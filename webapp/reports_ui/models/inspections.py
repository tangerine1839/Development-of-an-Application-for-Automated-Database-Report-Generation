# webapp/reports_ui/models/inspections.py
from django.db import models


class ReportInspectionParams(models.Model):
    title = models.CharField(max_length=200, default="Отчёт по инспекциям")
    status = models.JSONField(default=list)
    date_from = models.DateTimeField(null=True, blank=True)
    date_to = models.DateTimeField(null=True, blank=True)
    place_ids = models.JSONField(default=list)
    creator_ids = models.JSONField(default=list)
    assignee_ids = models.JSONField(default=list)
    is_guest = models.BooleanField(null=True, blank=True)
    columns = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title