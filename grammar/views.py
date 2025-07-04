from rest_framework import viewsets, filters
from .models import GrammarArticle
from .serializers import GrammarArticleSerializer

class GrammarArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GrammarArticle.objects.select_related('language').all()
    serializer_class = GrammarArticleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'section']
    ordering_fields = ['language', 'section', 'title', 'created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        lang = self.request.query_params.get('language')
        section = self.request.query_params.get('section')
        if lang:
            qs = qs.filter(language__code=lang)
        if section:
            qs = qs.filter(section__icontains=section)
        return qs
