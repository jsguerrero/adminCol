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


from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import formulario_usuario, formulario_direccion

def registro(request):
    if request.method == 'POST':
        form_usuario = formulario_usuario(request.POST)
        form_direccion = formulario_direccion(request.POST)
        #form_direccion.fields['cla_asentamiento'] = cat_asentamiento.objects.get(id=86104)
        #form_direccion['cla_asentamiento'] = (86104, cat_asentamiento.objects.get(id=86104))
        # Falta validar el formulario de la direccion marca error
        # Select a valid choice. That choice is not one of the available choices.
        if form_usuario.is_valid() and form_direccion.is_valid():
            #usuario = form_usuario.save(commit=False)
            direccion = form_direccion.save(commit=False)
            usuario = form_usuario.save()
            direccion.cla_usuario_id = usuario.id
            print(direccion)
            #print(form_direccion.cla_usuario_id)
            direccion.save()
            return HttpResponseRedirect('/usuarios/login')
        else:
            print (form_usuario.errors)
            print (form_direccion.errors)
    else:
        form_usuario = formulario_usuario()
        form_direccion = formulario_direccion()

    context={'form_usuario':form_usuario,
        'form_direccion':form_direccion
    }

    context.update(csrf(request))

    return render(request, 'registration/registro.html', context)


from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
def cargar_colonias(request):
    if request.is_ajax():
        codigo_postal = request.GET.get('codigo_postal')
        #asentamientos = cat_asentamiento.objects.none()
        #options = '<option value="" selected="selected">Seleccion Colonia</option>'
        if codigo_postal:
            criterio1 = Q(cla_codigo_postal=codigo_postal)
            criterio2 = Q(activo=1)
            asentamientos = cat_asentamiento.objects.filter(criterio1 & criterio2)
            query = "select concat(nom_tipo_asentamiento, ' ', nom_asentamiento) from colonias_cat_tipo_asentamiento where colonias_cat_tipo_asentamiento.cla_tipo_asentamiento = colonias_cat_asentamiento.cla_tipo_asentamiento_id"
            asentamientos = asentamientos.extra(select={'descripcion_asentamiento':query})
            #for asentamiento in asentamientos:
            #    options += '<option value="%s">%s</option>' % (
            #        asentamiento.cla_asentamiento,
            #        asentamiento.descripcion_asentamiento
            #    )
        #response = {}
        #response['cla_asentamiento'] = options
        #return JsonResponse(response)
        return render(request, 'asentamientos.html', {'asentamientos': asentamientos})
    else:
        return HttpResponseRedirect('/colonias/registro')
