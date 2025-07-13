from rest_framework import viewsets, filters

from api.mixins import QueryParamsFilterMixin
from .models import PhrasebookSection, PhrasebookPhrase
from .serializers import PhrasebookSectionSerializer, PhrasebookPhraseSerializer

class PhrasebookSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PhrasebookSection.objects.prefetch_related('phrases').all()
    serializer_class = PhrasebookSectionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class PhrasebookPhraseViewSet(QueryParamsFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = PhrasebookPhrase.objects.select_related('section').all()
    serializer_class = PhrasebookPhraseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'translation', 'translit', 'section__name']
    ordering_fields = ['section', 'id']

    query_params_map = {"section_id": "section_id"}
