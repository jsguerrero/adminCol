from django.contrib import admin

# Register your models here.

from .models import cat_codigo_postal, cat_pais, cat_estado, cat_municipio, cat_asentamiento, cat_tipo_asentamiento

admin.site.register(cat_codigo_postal)
admin.site.register(cat_pais)
admin.site.register(cat_estado)
admin.site.register(cat_municipio)
admin.site.register(cat_asentamiento)
admin.site.register(cat_tipo_asentamiento)
