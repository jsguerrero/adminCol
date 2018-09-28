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
#from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from .forms import formulario_usuario, formulario_direccion

def registro(request):
    if request.method == 'POST':
        form_usuario = formulario_usuario(request.POST)
        form_direccion = formulario_direccion(request.POST)
        col = request.POST.get('cla_asentamiento')
        form_direccion.fields['cla_asentamiento'].choices = [(col, col)]
        if form_usuario.is_valid() and form_direccion.is_valid():
            usuario = form_usuario.save(commit=False)
            form_direccion.fields['cla_usuario'] = usuario
            print(form_direccion.fields['cla_asentamiento'])
            #form_direccion.save()
            return HttpResponseRedirect('/usuarios/login')
        else:
            print (form_usuario.errors)
            print (form_direccion.errors)
    else:
        form_usuario = formulario_usuario()
        form_direccion = formulario_direccion()

    #context = {}
    #context.update(csrf(request))
    #context['form'] = formulario_registro()

    #context={'form':formulario_registro()
    #}
    context={'form_usuario':form_usuario,
        'form_direccion':form_direccion
    }

    context.update(csrf(request))

    return render(request, 'registration/registro.html', context)

from django.http import HttpResponse

def cargar_colonias(request):
    if request.is_ajax():
        codigo_postal = request.GET.get('codigo_postal')
        query = "select concat(nom_tipo_asentamiento, ' ', nom_asentamiento) from colonias_cat_tipo_asentamiento where colonias_cat_tipo_asentamiento.cla_tipo_asentamiento = colonias_cat_asentamiento.cla_tipo_asentamiento_id"
        asentamientos = cat_asentamiento.objects.filter(cla_codigo_postal=codigo_postal).order_by('nom_asentamiento')
        asentamientos = asentamientos.extra(
            select={'descripcion_asentamiento':query})
        #estado = cat_estado.objects.filter(cat_codigo_postal=codigo_postal)
        return render(request, 'asentamientos.html', {'asentamientos': asentamientos})
    else:
        return HttpResponseRedirect('/colonias/registro')
