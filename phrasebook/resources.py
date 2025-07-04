from import_export import resources
from .models import PhrasebookSection, PhrasebookPhrase

class PhrasebookSectionResource(resources.ModelResource):
    class Meta:
        model = PhrasebookSection

class PhrasebookPhraseResource(resources.ModelResource):
    class Meta:
        model = PhrasebookPhrase
