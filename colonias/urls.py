from django.conf.urls import url
#from django.contrib import admin
#from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('registro/', views.registro, name='registro'),
  path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
  path('necesita_validacion/', views.necesita_validacion, name='necesita_validacion'),
  re_path('confirm/(?P<llave_activacion>\w+)/', views.activacion_cuenta),
  path('ajax/cargar_colonias/', views.cargar_colonias, name='ajax_cargar_colonias'),
]
