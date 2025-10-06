from django.db.utils import OperationalError, ProgrammingError
from django.utils import timezone

from .models import Visit


class TrackVisitMiddleware:
    """Persist session activity for analytics."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            session_key = request.session.session_key
            if not session_key:
                request.session.save()
                session_key = request.session.session_key
        except (OperationalError, ProgrammingError):
            return response

        ip = request.META.get("REMOTE_ADDR", "0.0.0.0")
        now = timezone.now()
        today = now.date()

        try:
            visit, created = Visit.objects.get_or_create(
                session_key=session_key,
                date=today,
                defaults={"ip_address": ip, "last_activity": now},
            )
        except (OperationalError, ProgrammingError):
            return response

        if not created:
            visit.last_activity = now
            visit.ip_address = ip
            visit.save(update_fields=["last_activity", "ip_address"])

        return response
