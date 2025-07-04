from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import PhrasebookSection, PhrasebookPhrase

class PhrasebookSectionResource(resources.ModelResource):
    class Meta:
        model = PhrasebookSection

class PhrasebookPhraseResource(resources.ModelResource):
    class Meta:
        model = PhrasebookPhrase

@admin.register(PhrasebookSection)
class PhrasebookSectionAdmin(ImportExportModelAdmin):
    resource_class = PhrasebookSectionResource
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(PhrasebookPhrase)
class PhrasebookPhraseAdmin(ImportExportModelAdmin):
    resource_class = PhrasebookPhraseResource
    list_display = ('text', 'translation', 'translit', 'section')
    search_fields = ('text', 'translation', 'translit', 'section__name')
    list_filter = ('section',)
