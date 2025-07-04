from rest_framework import serializers
from .models import Language, Word, Translation, Example, Synonym

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'code', 'name')

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'text', 'translation', 'source')

class WordShortSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)
    class Meta:
        model = Word
        fields = ('id', 'text', 'language', 'part_of_speech', 'transcription')

class TranslationSerializer(serializers.ModelSerializer):
    from_word = WordShortSerializer(read_only=True)
    to_word = WordShortSerializer(read_only=True)
    class Meta:
        model = Translation
        fields = ('id', 'from_word', 'to_word', 'quality', 'notes')

class SynonymSerializer(serializers.ModelSerializer):
    word1 = WordShortSerializer(read_only=True)
    word2 = WordShortSerializer(read_only=True)
    class Meta:
        model = Synonym
        fields = ('id', 'word1', 'word2')

class WordSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)
    translations = serializers.SerializerMethodField()
    examples = ExampleSerializer(many=True, read_only=True)
    synonyms = serializers.SerializerMethodField()

    class Meta:
        model = Word
        fields = (
            'id', 'text', 'language', 'part_of_speech', 'transcription',
            'alternative_spelling', 'lemma', 'description',
            'translations', 'examples', 'synonyms',
            'created_at', 'updated_at'
        )

    def get_translations(self, obj):
        translations = obj.translations_from.select_related('to_word', 'to_word__language')
        return TranslationSerializer(translations, many=True).data

    def get_synonyms(self, obj):
        synonyms1 = obj.synonyms1.select_related('word2', 'word2__language')
        synonyms2 = obj.synonyms2.select_related('word1', 'word1__language')
        # показываем обе стороны связи, исключаем дубли
        synonym_words = set([s.word2 for s in synonyms1] + [s.word1 for s in synonyms2])
        return WordShortSerializer(synonym_words, many=True).data
