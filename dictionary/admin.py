from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Language, Word, Translation, Example, Synonym, PartOfSpeech
from import_export import resources

class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language

class WordResource(resources.ModelResource):
    class Meta:
        model = Word

class PartOfSpeechResource(resources.ModelResource):
    class Meta:
        model = PartOfSpeech

class TranslationResource(resources.ModelResource):
    class Meta:
        model = Translation

class ExampleResource(resources.ModelResource):
    class Meta:
        model = Example

class SynonymResource(resources.ModelResource):
    class Meta:
        model = Synonym

@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource
    search_fields = ('code', 'name')
    list_display = ('code', 'name')

@admin.register(Word)
class WordAdmin(ImportExportModelAdmin):
    resource_class = WordResource
    search_fields = ('text',)
    list_display = ('text', 'language', 'part_of_speech', 'transcription')

@admin.register(Translation)
class TranslationAdmin(ImportExportModelAdmin):
    autocomplete_fields = ['from_word', 'to_word']
    resource_class = TranslationResource
    list_display = ('from_word', 'to_word', 'quality')

@admin.register(Example)
class ExampleAdmin(ImportExportModelAdmin):
    resource_class = ExampleResource
    list_display = ('text', 'word', 'translation', 'source')

@admin.register(Synonym)
class SynonymAdmin(ImportExportModelAdmin):
    resource_class = SynonymResource
    list_display = ('word1', 'word2')
