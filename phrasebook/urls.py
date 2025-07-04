from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhrasebookSectionViewSet, PhrasebookPhraseViewSet

router = DefaultRouter()
router.register('sections', PhrasebookSectionViewSet)
router.register('phrases', PhrasebookPhraseViewSet)

urlpatterns = router.urls
