from rest_framework.routers import DefaultRouter
from .views import GrammarArticleViewSet

router = DefaultRouter()
router.register('articles', GrammarArticleViewSet)

urlpatterns = router.urls
