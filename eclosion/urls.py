from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('bande', views.bande, name = 'bande'),
    path('local', views.local, name = 'local'),
    path('contact', views.contact, name = 'contact'),
    path('detail', views.detail, name = 'detail'),
    path('shop', views.shop, name = 'shop'),
    path('more', views.more, name = 'more'),
    path('actus', views.actus, name = 'actus'),
    path('ProjectDeveloppement', views.ProjectDeveloppement, name = 'Projects en developpement'),
    path('ProjectProduction', views.ProjectProduction, name = 'Projects en production'),
    path('ProjectPostprod', views.ProjectPostprod, name = 'Projects en post-production'),
    path('Series', views.series, name = 'Series'),
    path('Documentaires', views.docs, name = 'Documentaires'),
    path('Fiction long metrage', views.FLM, name = 'Fiction long metrage'),
    path('Fiction court metrage', views.FCM, name = 'Fiction court metrage'),
    path('Reportages', views.reportages, name = 'Reportages'),
   
]