from rest_framework import serializers
from .models import GrammarArticle
from dictionary.serializers import LanguageSerializer

class GrammarArticleSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = GrammarArticle
        fields = (
            'id', 'title', 'content', 'language', 'section',
            'created_at', 'updated_at'
        )
