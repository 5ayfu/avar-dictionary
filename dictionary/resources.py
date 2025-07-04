from import_export import resources
from .models import Language, Word, Translation, Example, Synonym

class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language

class WordResource(resources.ModelResource):
    class Meta:
        model = Word

class TranslationResource(resources.ModelResource):
    class Meta:
        model = Translation

class ExampleResource(resources.ModelResource):
    class Meta:
        model = Example

class SynonymResource(resources.ModelResource):
    class Meta:
        model = Synonym
