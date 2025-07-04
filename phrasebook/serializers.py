from rest_framework import serializers
from .models import PhrasebookSection, PhrasebookPhrase

class PhrasebookPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhrasebookPhrase
        fields = ('id', 'section', 'text', 'translation', 'translit')

class PhrasebookSectionSerializer(serializers.ModelSerializer):
    phrases = PhrasebookPhraseSerializer(many=True, read_only=True)

    class Meta:
        model = PhrasebookSection
        fields = ('id', 'name', 'phrases')
