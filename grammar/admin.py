from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import GrammarArticle

class GrammarArticleResource(resources.ModelResource):
    class Meta:
        model = GrammarArticle

@admin.register(GrammarArticle)
class GrammarArticleAdmin(ImportExportModelAdmin):
    resource_class = GrammarArticleResource
    list_display = ('title', 'language', 'section', 'created_at')
    search_fields = ('title', 'content', 'section')
    list_filter = ('language', 'section')
