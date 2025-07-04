from rest_framework import viewsets, filters
from .models import PhrasebookSection, PhrasebookPhrase
from .serializers import PhrasebookSectionSerializer, PhrasebookPhraseSerializer

class PhrasebookSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PhrasebookSection.objects.prefetch_related('phrases').all()
    serializer_class = PhrasebookSectionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class PhrasebookPhraseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PhrasebookPhrase.objects.select_related('section').all()
    serializer_class = PhrasebookPhraseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'translation', 'translit', 'section__name']
    ordering_fields = ['section', 'id']

    def get_queryset(self):
        qs = super().get_queryset()
        section_id = self.request.query_params.get('section_id')
        if section_id:
            qs = qs.filter(section_id=section_id)
        return qs
