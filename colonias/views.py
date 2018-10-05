from django.shortcuts import render

# Create your views here.

from .models import cat_codigo_postal, cat_pais, cat_estado, cat_municipio, cat_asentamiento
#from .models import cat_direccion_usuario
def index(request):
    """
    Vista para la pagina de inicio
    """

    num_codigos_postales = 0
    num_paises = 0
    num_estados = 0
    num_municipios = 0
    num_asentamientos = 0

    if request.user.is_authenticated:
        num_codigos_postales = cat_pais.objects.all().count()
        num_paises = cat_pais.objects.all().count()
        num_estados = cat_estado.objects.all().count()
        num_municipios = cat_municipio.objects.all().count()
        num_asentamientos = cat_asentamiento.objects.all().count() #cat_direccion_usuario.objects.get(cla_usuario_id = request.user.id).nom_calle

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
from django.core.mail import send_mail
import hashlib, random, datetime
from django.utils import timezone
from .models import cat_usuario, perfil_usuario

def registro(request):
    if request.method == 'POST':
        form_usuario = formulario_usuario(request.POST)
        form_direccion = formulario_direccion(request.POST)
        if form_usuario.is_valid() and form_direccion.is_valid():
            direccion = form_direccion.save(commit=False)
            usuario = form_usuario.save()
            direccion.cla_usuario_id = usuario.id
            direccion.activo = False
            direccion.cla_codigo_postal_id = cat_codigo_postal.objects.get(cla_codigo_postal = form_direccion.cleaned_data['codigo_postal'])
            direccion.save()
            email = form_usuario.cleaned_data['email']
            sem = hashlib.sha1(str(random.random()).encode("utf-8")).hexdigest()[:5]
            llave_activacion = hashlib.sha1((sem+email).lower().encode("utf-8")).hexdigest()
            expiracion_llave = timezone.now() + timezone.timedelta(days=2)
            u = cat_usuario.objects.get(email=email)
            perfil = perfil_usuario(cla_usuario=u, llave_activacion=llave_activacion, expiracion_llave=expiracion_llave)
            perfil.save()
            asunto_email = 'Confirmación de cuenta.'
            cuerpo_email = "Gracias por registrarte. Para activar tu cuenta da click en este enlace en menos de 48 hrs.  http://10.1.103.90:8000/colonias/confirm/%s" % (llave_activacion)
            cuenta_correo = 'sg@resepa.com'
            send_mail(asunto_email, cuerpo_email, cuenta_correo, [email], fail_silently=False)
            context={'correo':email}
            return render(request, 'registration/necesita_validacion.html', context)

            #return HttpResponseRedirect('/colonias/necesita_validacion')
        # Se limpia el formulario de direccion
        # django.core.exceptions.FieldError: Cannot resolve keyword 'name' into field.
        # No permite redireccionar con datos en el formulario de direccion
        # No se que se debe hacer para respetar el codigo postal ya buscado
        else :
            form_direccion = formulario_direccion()
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
        if codigo_postal:
            criterio1 = Q(cla_codigo_postal=codigo_postal)
            criterio2 = Q(activo=1)
            asentamientos = cat_asentamiento.objects.filter(criterio1 & criterio2)
            query = "select concat(nom_tipo_asentamiento, ' ', nom_asentamiento) from colonias_cat_tipo_asentamiento where colonias_cat_tipo_asentamiento.cla_tipo_asentamiento = colonias_cat_asentamiento.cla_tipo_asentamiento_id"
            asentamientos = asentamientos.extra(select={'descripcion_asentamiento':query})
        return render(request, 'asentamientos.html', {'asentamientos': asentamientos})
    else:
        return HttpResponseRedirect('/colonias/registro')

from django.shortcuts import get_object_or_404
def activacion_cuenta(request, llave_activacion):
    if request.user.is_authenticated:
        HttpResponseRedirect('/')

    perfil = get_object_or_404(perfil_usuario, llave_activacion=llave_activacion)

    if perfil.expiracion_llave < timezone.now():
        return HttpResponseRedirect('/')

    usuario = perfil.cla_usuario
    usuario.is_active = True
    usuario.save()
    return HttpResponseRedirect('/usuarios/login')

def necesita_validacion(request):
    return render(request, 'registration/necesita_validacion.html')


from .forms import formulario_editar_usuario, formulario_direcciones_usuario
from .models import perfil_vecino
from django.forms import inlineformset_factory
def editar_usuario(request):
    usuario = cat_usuario.objects.get(id=request.user.id)
    direcciones_formset = inlineformset_factory(cat_usuario,
                                                perfil_vecino,
                                                form=formulario_direcciones_usuario,
                                                extra=1)
    #if form_usuario.is_valid():
    #    return render(request, 'registration/necesita_validacion.html', context)
    form_usuario = formulario_editar_usuario(instance=usuario)
    formset = direcciones_formset(instance=usuario)
    context={'formset': formset,'form':form_usuario
    }

    context.update(csrf(request))

    return render(request, 'registration/editar_usuario.html', context)

