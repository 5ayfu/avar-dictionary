from datetime import timedelta
from django.utils import timezone
from .models import Visit


def analytics(_request):
    """Provide visitor statistics for templates."""
    now = timezone.now()
    five_minutes_ago = now - timedelta(minutes=5)

    active = Visit.objects.filter(last_activity__gte=five_minutes_ago).count()
    unique_today = Visit.objects.filter(date=now.date()).count()
    return {
        "active_visitors": active,
        "unique_visitors_today": unique_today,
    }
