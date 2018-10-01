from django.contrib import admin

# Register your models here.

from .models import cat_codigo_postal, cat_pais, cat_estado, cat_municipio
from .models import cat_asentamiento, cat_tipo_asentamiento, cat_usuario
from .models import cat_direccion_usuario

admin.site.register(cat_codigo_postal)
admin.site.register(cat_pais)
admin.site.register(cat_estado)
admin.site.register(cat_municipio)
#admin.site.register(cat_asentamiento)
admin.site.register(cat_tipo_asentamiento)
admin.site.register(cat_direccion_usuario)

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

class cat_usuarioAdmin(UserAdmin):
    class Meta:
        model = cat_usuario

    add_fieldsets = (
        ('Cuenta',{
            'fields':('email',
                      'password1',
                      'password2')
        }),
        ('Información Personal',{
            'fields':('nom_usuario',
                      'apellido_paterno',
                      'apellido_materno')
        }),
        ('Permisos',{
            'fields':('is_staff',
                      'is_active',
                      'es_admin',
                      'es_guardia')
        }),
    )

    fieldsets = (
        ('Cuenta',{
            'fields':('email',
                      'password')
        }),
        ('Información Personal',{
            'fields':('nom_usuario',
                      'apellido_paterno',
                      'apellido_materno',
                      'cla_asentamiento')
        }),
        ('Permisos',{
            'fields':('is_staff',
                      'is_active',
                      'es_admin',
                      'es_guardia')
        }),
    )

    list_display = ('email', 'nom_usuario', 'apellido_paterno', 'apellido_materno', 'es_admin', 'es_guardia')

    ordering = ('email',)

admin.site.unregister(Group)
admin.site.register(cat_usuario, cat_usuarioAdmin)

def activar_asentamientos(modeladmin, request, queryset):
    queryset.update(activo=1)
activar_asentamientos.short_description = "Marcar como activos"

class cat_asentamientoAdmin(admin.ModelAdmin):
    list_display = ('nom_asentamiento', 'cla_codigo_postal','activo')

    search_fields = ['nom_asentamiento', 'cla_codigo_postal__exact']

    actions = [activar_asentamientos]

admin.site.register(cat_asentamiento, cat_asentamientoAdmin)
