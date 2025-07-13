from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

from api.mixins import QueryParamsFilterMixin
from .models import Language, Word, Translation, Example, Synonym
from .serializers import (
    LanguageSerializer,
    WordSerializer,
    WordShortSerializer,
    TranslationSerializer,
    ExampleSerializer,
    SynonymSerializer,
)

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    pagination_class = None

class WordViewSet(QueryParamsFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Word.objects.all().select_related('language', 'lemma').prefetch_related('translations_from', 'examples', 'synonyms1', 'synonyms2')
    serializer_class = WordSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'transcription', 'alternative_spelling', 'description']
    ordering_fields = ['text', 'created_at']

    query_params_map = {
        "language": "language__code",
        "part_of_speech": "part_of_speech",
    }

class TranslationViewSet(QueryParamsFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Translation.objects.select_related('from_word', 'to_word', 'from_word__language', 'to_word__language').all()
    serializer_class = TranslationSerializer

    query_params_map = {
        "from_word_id": "from_word_id",
        "to_word_id": "to_word_id",
    }

class ExampleViewSet(QueryParamsFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Example.objects.select_related('word').all()
    serializer_class = ExampleSerializer
    query_params_map = {"word_id": "word_id"}

class SynonymViewSet(QueryParamsFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Synonym.objects.select_related('word1', 'word2').all()
    serializer_class = SynonymSerializer

    query_params_map = {
        "word_id": lambda qs, value: qs.filter(Q(word1_id=value) | Q(word2_id=value)),
    }

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
