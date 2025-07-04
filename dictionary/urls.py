from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LanguageViewSet, WordViewSet, TranslationViewSet,
    ExampleViewSet, SynonymViewSet, search_words, quick_translate
)

router = DefaultRouter()
router.register('languages', LanguageViewSet)
router.register('words', WordViewSet)
router.register('translations', TranslationViewSet)
router.register('examples', ExampleViewSet)
router.register('synonyms', SynonymViewSet)

urlpatterns = [
    path('search/', search_words, name='word-search'),
    path('translate/', quick_translate, name='quick-translate'),
]
urlpatterns += router.urls
