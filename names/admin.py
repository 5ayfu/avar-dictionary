from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import AvarName, NameCategory


class NameCategoryResource(resources.ModelResource):
    class Meta:
        model = NameCategory
        fields = ('id', 'name', 'description', 'order')


class AvarNameResource(resources.ModelResource):
    class Meta:
        model = AvarName
        fields = (
            'id',
            'category__name',
            'name',
            'translation',
            'translit',
            'gender',
            'notes',
            'created_at',
            'updated_at',
        )


@admin.register(NameCategory)
class NameCategoryAdmin(ImportExportModelAdmin):
    resource_class = NameCategoryResource
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)


@admin.register(AvarName)
class AvarNameAdmin(ImportExportModelAdmin):
    resource_class = AvarNameResource
    list_display = ('name', 'translation', 'gender', 'category')
    list_filter = ('category', 'gender')
    search_fields = ('name', 'translation', 'translit', 'notes', 'category__name')
    autocomplete_fields = ('category',)
