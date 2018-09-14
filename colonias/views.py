from django.shortcuts import render

# Create your views here.

from .models import cat_codigo_postal, cat_pais, cat_estado, cat_municipio, cat_asentamiento

def index(request):
    """
    Vista para la pagina de inicio
    """

    num_codigos_postales = cat_pais.objects.all().count()
    num_paises = cat_pais.objects.all().count()
    num_estados = cat_estado.objects.all().count()
    num_municipios = cat_municipio.objects.all().count()
    num_asentamientos = cat_asentamiento.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_codigos_postales':num_codigos_postales,
                 'num_paises':num_paises,
                 'num_estados':num_estados,
                 'num_municipios':num_municipios,
                 'num_asentamientos':num_asentamientos
        },
    )
