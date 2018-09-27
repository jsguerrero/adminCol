from django.conf.urls import url
#from django.contrib import admin
#from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^registro/$', views.registro, name='registro'),
  path('ajax/cargar_colonias/', views.cargar_colonias, name='ajax_cargar_colonias'),
]
