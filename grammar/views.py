from rest_framework import viewsets, filters

from api.mixins import QueryParamsFilterMixin
from .models import GrammarArticle
from .serializers import GrammarArticleSerializer

class GrammarArticleViewSet(QueryParamsFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = GrammarArticle.objects.select_related('language').all()
    serializer_class = GrammarArticleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'section']
    ordering_fields = ['language', 'section', 'title', 'created_at']

    query_params_map = {
        "language": "language__code",
        "section": "section__icontains",
    }
