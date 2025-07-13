from typing import Mapping
from django.db.models import QuerySet

class QueryParamsFilterMixin:
    """Filter a queryset based on request query parameters."""
    query_params_map: Mapping[str, str] = {}

    def filter_queryset_by_params(self, queryset: QuerySet) -> QuerySet:
        for param, lookup in self.query_params_map.items():
            value = self.request.query_params.get(param)
            if value:
                queryset = queryset.filter(**{lookup: value})
        return queryset

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_queryset_by_params(queryset)
