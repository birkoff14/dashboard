from django.urls import path
from reportinfra import views
from django.contrib import admin
from django.conf.urls import url
from .ajax import get_componentes, get_vendors, get_folder
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
    url(r'^ajax/get_folder/$', get_folder, name='get_folder'),  
    path('api', ActivitiesListApiView.as_view()), 
    path('reporteSemanal', views.reporteSemanal, name='reporteSemanal'),
    path('detailSemanal/<str:fecha>/<str:usuario>', views.detailSemanal, name='detailSemanal'),
    path('projects', views.projects, name='projects'),
    path('addProject/<str:idP>', views.addProject, name='addProject'),
    path('editProject/<str:idP>', views.editProject, name='editProject'),
    path('keepass/', views.keepass, name='keepass'),
    path('keepass_load/', views.keepass_load, name='keepass_load'),
    path('get_info/', views.get_info, name='get_info'),
    path('get_info_detail/', views.get_info_detail, name='get_info_detail'),
    path('addKeepass/', views.addKeepass, name='addKeepass'),
    path('editKeepass/<str:idK>', views.editKeepass, name='editKeepass'),
]

admin.site.site_header = "Operación de Aplicaciones Cloud"
