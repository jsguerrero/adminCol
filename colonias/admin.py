from django.contrib import admin

# Register your models here.

from .models import CodigoPostal, Pais, Estado, Municipio, Colonia

admin.site.register(CodigoPostal)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Colonia)
