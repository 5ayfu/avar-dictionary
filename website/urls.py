from django.urls import path
from django.views.generic import TemplateView

from .views import AboutView, PhrasebookView


urlpatterns = [
    path('', TemplateView.as_view(template_name='website/index.html'), name='home'),
    path('dictionary/', TemplateView.as_view(template_name='website/dictionary.html'), name='dictionary'),
    path('phrasebook/', PhrasebookView.as_view(), name='phrasebook'),
    path('grammar/', TemplateView.as_view(template_name='website/grammar.html'), name='grammar'),
    path('names/', TemplateView.as_view(template_name='website/names.html'), name='names'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', TemplateView.as_view(template_name='website/contact.html'), name='contact'),
]
