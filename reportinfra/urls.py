from django.urls import path
from reportinfra import views
from django.contrib import admin
from django.conf.urls import url
from .ajax import get_componentes, get_vendors
from .views import (
    ActivitiesListApiView,
)


urlpatterns = [
    path('', views.login, name='login'),
    path("logout", views.logout, name="logout"),
    path('main', views.main, name='main'),
    path('sr', views.sr, name='sr'),
    path('reportes', views.reportes, name='reportes'),
    path('kpis', views.kpis, name='kpis'),
    path('detailSR/<str:idSR>', views.detailSR, name='detailSR'),
    path('cierre/<str:idSR>', views.cierre, name='cierre'),
    path('editSR/<str:idSR>', views.editSR, name='editSR'),
    path('editActivity/<str:idAct>/<str:idU>', views.editActivity, name='editActivity'),
    path('recover', views.recover, name='recover'),
    path('actividades', views.activity, name='actividades'),
    path('repactividades', views.repactividades, name='repactividades'),
    url(r'^ajax/get_componentes/$', get_componentes, name='get_componentes'),  
    url(r'^ajax/get_vendors/$', get_vendors, name='get_vendors'),     
    path('api', ActivitiesListApiView.as_view()), 
    path('reporteSemanal', views.reporteSemanal, name='reporteSemanal'),
    path('detailSemanal/<str:fecha>/<str:usuario>', views.detailSemanal, name='detailSemanal'),

]

admin.site.site_header = "Operación de Aplicaciones Cloud"
