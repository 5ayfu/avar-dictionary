from django.contrib import admin
from .models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("session_key", "ip_address", "date", "last_activity")
    search_fields = ("session_key", "ip_address")
