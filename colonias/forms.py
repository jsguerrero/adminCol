from django.forms import ModelForm, CharField, TextInput, PasswordInput, IntegerField, ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .models import cat_usuario

class formulario_usuario(ModelForm):

    class Meta:
        model = cat_usuario
        fields = ['email', 'contrasena1', 'contrasena2', 'nom_usuario', 'apellido_paterno', 'apellido_materno']
        widgets = {'email':TextInput(attrs={'placeholder':'Correo electrónico'}),
                   'nom_usuario':TextInput(attrs={'placeholder':'Nombre(s)'}),
                   'apellido_paterno':TextInput(attrs={'placeholder':'Apellido Paterno'}),
        }

    contrasena1 = CharField(required=True,
                                  label='Contraseña',
                                  help_text='Mínimo 8 caracteres con mayúscula, minúscula y número o caracter especial',
                                  widget=PasswordInput(
                                      attrs={'id':'contrasena1',
                                             'placeholder':'Contraseña',
                                             'pattern':'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                      }))

    contrasena2 = CharField(required=True,
                                  label='Confirmar contraseña',
                                  help_text='Mínimo 8 caracteres con mayúscula, minúscula y número o caracter especial',
                                  widget=PasswordInput(
                                      attrs={
                                          'placeholder':'Confirmar contraseña',
                                          'pattern':'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                      }))

    apellido_materno = CharField(max_length=50,
                                       label='Apellido Materno',
                                       required=False,
                                       widget=TextInput(
                                           attrs={'placeholder':'Apellido Materno'}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            cat_usuario.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise ValidationError('Ese correo ya está en uso.')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["contrasena1"])
        if commit:
            usuario.is_active = False
            usuario.save()
        return usuario

from django.forms import ModelChoiceField, Select
from .models import perfil_vecino, cat_asentamiento, cat_codigo_postal
class formulario_direccion(ModelForm):

    class Meta:
        model = perfil_vecino
        fields = ['codigo_postal', 'cla_asentamiento', 'nom_calle', 'num_exterior', 'num_interior']
        widgets = {'nom_calle':TextInput(attrs={'placeholder':'Calle'}),
                   'num_exterior':TextInput(attrs={'placeholder':'Número Exterior'}),
                   'num_interior':TextInput(attrs={'placeholder':'Número Interior'})
        }

    codigo_postal = IntegerField(label='Código Postal',
                                       required=True,
                                       widget=TextInput(
                                           attrs={
                                               'placeholder':'Código Postal',
                                               'pattern':'(\d{5}?)'
                                           }))

    cla_asentamiento = ModelChoiceField(
        label=u'Colonias',
        required=True,
        queryset=cat_asentamiento.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super(formulario_direccion, self).__init__(*args, **kwargs)
        self.fields['cla_asentamiento'].queryset = cat_asentamiento.objects.none()

        if 'codigo_postal' in self.data:
            try:
                cla_codigo_postal = self.data.get('codigo_postal')
                self.fields['cla_asentamiento'].queryset = cat_asentamiento.objects.filter(cla_codigo_postal=cla_codigo_postal).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['cla_asentamiento'].queryset = self.instance.codig_postal.cla_asentamiento_set.order_by('name')


class formulario_editar_usuario(ModelForm):

    class Meta:
        model = cat_usuario
        fields = ['email', 'nom_usuario', 'apellido_paterno', 'apellido_materno']
        widgets = {'email':TextInput(attrs={'placeholder':'Correo electrónico'}),
                   'nom_usuario':TextInput(attrs={'placeholder':'Nombre(s)'}),
                   'apellido_paterno':TextInput(attrs={'placeholder':'Apellido Paterno'}),
        }

    apellido_materno = CharField(max_length=50,
                                       label='Apellido Materno',
                                       required=False,
                                       widget=TextInput(
                                           attrs={'placeholder':'Apellido Materno'}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            cat_usuario.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise ValidationError('Ese correo ya está en uso.')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["contrasena1"])
        if commit:
            usuario.is_active = False
            usuario.save()
        return usuario

from .models import perfil_vecino
from django.forms import inlineformset_factory
#https://stackoverflow.com/questions/980405/raw-id-fields-for-modelforms
class formulario_direcciones_usuario(ModelForm):
    class Meta:
        model = perfil_vecino
        exclude = ()
