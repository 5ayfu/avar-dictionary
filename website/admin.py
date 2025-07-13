from django.contrib import admin
from .models import Visit, ProjectInfo


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("session_key", "ip_address", "date", "last_activity")
    search_fields = ("session_key", "ip_address")


@admin.register(ProjectInfo)
class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
