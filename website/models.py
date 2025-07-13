from django.db import models


class Visit(models.Model):
    """Store information about a user's visit for simple analytics."""

    session_key = models.CharField(max_length=40)
    ip_address = models.GenericIPAddressField()
    date = models.DateField()
    last_activity = models.DateTimeField()

    class Meta:
        unique_together = ("session_key", "date")
        indexes = [
            models.Index(fields=["last_activity"]),
            models.Index(fields=["date"]),
        ]

    def __str__(self) -> str:
        return f"{self.session_key} @ {self.date}"

