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


class ProjectInfo(models.Model):
    """Content for the About page editable via the admin."""

    title = models.CharField("Заголовок", max_length=256, default="О проекте")
    content = models.TextField("Описание")
    updated_at = models.DateTimeField("Изменено", auto_now=True)

    class Meta:
        verbose_name = "Информация о проекте"
        verbose_name_plural = "Информация о проекте"

    def __str__(self) -> str:
        return self.title

