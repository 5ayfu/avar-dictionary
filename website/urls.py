from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('phrasebook/', views.phrasebook, name='phrasebook'),
    path('grammar/', views.grammar, name='grammar'),
    path('names/', views.names, name='names'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
