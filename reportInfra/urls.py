from django.urls import path
from reportInfra import views
from django.contrib import admin
from django.conf.urls import url
from .ajax import get_componentes, get_vendors


urlpatterns = [
    path('', views.login, name='login'),
    path("logout", views.logout, name="logout"),
    path('main', views.main, name='main'),
    path('sr', views.sr, name='sr'),
    path('reportes', views.reportes, name='reportes'),
    path('kpis', views.kpis, name='kpis'),
    path('detailSR/<str:idSR>', views.detailSR, name='detailSR'),
    path('cierre/<str:idSR>', views.cierre, name='cierre'),
    url(r'^ajax/get_componentes/$', get_componentes, name='get_componentes'),  
    url(r'^ajax/get_vendors/$', get_vendors, name='get_vendors'),          
]

admin.site.site_header = "Operación de Aplicaciones Cloud"