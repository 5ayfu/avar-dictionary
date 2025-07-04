from rest_framework import viewsets, generics, filters, mixins
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import Language, Word, Translation, Example, Synonym
from .serializers import (
    LanguageSerializer, WordSerializer, WordShortSerializer,
    TranslationSerializer, ExampleSerializer, SynonymSerializer
)
from django.db.models import Q

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    pagination_class = None

class WordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Word.objects.all().select_related('language', 'lemma').prefetch_related('translations_from', 'examples', 'synonyms1', 'synonyms2')
    serializer_class = WordSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'transcription', 'alternative_spelling', 'description']
    ordering_fields = ['text', 'created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        lang = self.request.query_params.get('language')
        part = self.request.query_params.get('part_of_speech')
        if lang:
            qs = qs.filter(language__code=lang)
        if part:
            qs = qs.filter(part_of_speech=part)
        return qs

class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Translation.objects.select_related('from_word', 'to_word', 'from_word__language', 'to_word__language').all()
    serializer_class = TranslationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        from_word = self.request.query_params.get('from_word_id')
        to_word = self.request.query_params.get('to_word_id')
        if from_word:
            qs = qs.filter(from_word_id=from_word)
        if to_word:
            qs = qs.filter(to_word_id=to_word)
        return qs

class ExampleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Example.objects.select_related('word').all()
    serializer_class = ExampleSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        word_id = self.request.query_params.get('word_id')
        if word_id:
            qs = qs.filter(word_id=word_id)
        return qs

class SynonymViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Synonym.objects.select_related('word1', 'word2').all()
    serializer_class = SynonymSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        word_id = self.request.query_params.get('word_id')
        if word_id:
            qs = qs.filter(Q(word1_id=word_id) | Q(word2_id=word_id))
        return qs

# Поиск по слову с фильтрами
@api_view(['GET'])
def search_words(request):
    q = request.GET.get('q', '').strip()
    lang = request.GET.get('language')
    qs = Word.objects.select_related('language').all()
    if q:
        qs = qs.filter(
            Q(text__icontains=q) |
            Q(transcription__icontains=q) |
            Q(alternative_spelling__icontains=q) |
            Q(description__icontains=q)
        )
    if lang:
        qs = qs.filter(language__code=lang)
    serializer = WordShortSerializer(qs[:30], many=True)
    return Response(serializer.data)

# Быстрый перевод (от слова к переводам)
@api_view(['GET'])
def quick_translate(request):
    word = request.GET.get('word', '').strip()
    src = request.GET.get('from')
    tgt = request.GET.get('to')
    if not (word and src and tgt):
        return Response({'error': 'Required: word, from, to'}, status=400)
    word_obj = Word.objects.filter(text__iexact=word, language__code=src).first()
    if not word_obj:
        return Response([])
    translations = Translation.objects.filter(
        from_word=word_obj, to_word__language__code=tgt
    ).select_related('to_word', 'to_word__language')
    serializer = TranslationSerializer(translations, many=True)
    return Response(serializer.data)
