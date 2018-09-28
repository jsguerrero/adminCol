#from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CharField, TextInput, PasswordInput, IntegerField, ChoiceField, Select
from .models import cat_usuario
#from django import forms

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
    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["contrasena1"])
        if commit:
            usuario.save()
        return usuario

'''    def clean(self):
        datos = super().clean()
        correo_electronico = datos.get("correo_electronico")
        contrasena1 = datos.get("contrasena1")
        contrasena2 = datos.get("contrasena2")
        estado = datos.get("estado")
        colonia = datos.get("colonia")
        if correo_electronico or not contrasena1 or not contrasena2 or not estado:
            raise forms.ValidationError('Faltan datos necesarios')
        if colonia == 'Prueba':
            raise forms.ValidationError('Las contraseñas no coinciden')

    def guardar(self, commit=True):
        usuario = super(formulario_registro, self).guardar(commit=False)
        usuario.email = self.cleaned_data['email']

        if commit:
            user.guardar()

        return usuario
'''

from .models import cat_direccion_usuario, cat_asentamiento
class formulario_direccion(ModelForm):

    class Meta:
        model = cat_direccion_usuario
        fields = ['codigo_postal', 'cla_asentamiento', 'nom_calle', 'num_exterior', 'num_interior']
        widgets = {'nom_calle':TextInput(attrs={'placeholder':'Calle'}),
                   'num_exterior':TextInput(attrs={'placeholder':'Número Exterior'}),
                   'num_interior':TextInput(attrs={'placeholder':'Número Interior'}),
        #           'apellido_materno':TextInput(attrs={'placeholder':'Apellido Materno'}),
        }

    def __init__(self, *args, **kwargs):
        super(formulario_direccion, self).__init__(*args, **kwargs)
        self.fields['cla_asentamiento'].queryset = cat_asentamiento.objects.all()[0]

    codigo_postal = IntegerField(label='Código Postal',
                                       required=True,
                                       widget=TextInput(
                                           attrs={
                                               'placeholder':'Código Postal',
                                               'onfocusout':'validar_codigo_postal(this)',
                                               'pattern':'(\d{5}?)'
                                           }))

    cla_asentamiento = ChoiceField(label='Colonia',
                                required=True,
                                widget=Select(
                                 attrs={
                                     'required':' True'
                                 }))

    def save(self, commit=True):
        direccion = super().save(commit=False)
        cla_asentamiento_sel = self.cleaned_data["cla_asentamiento"]
        cla_asentamiento = cat_asentamiento.objects.filter(id=cla_asentamiento_sel)
        direccion.set_cla_asentamiento(cla_asentamiento)
        if commit:
            direccion.save()
        return direccion

    '''calle = forms.CharField(max_length=50,
                            label='Calle',
                            required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder':'Calle'
                                }))

    numero_ext = forms.CharField(max_length=50,
                            label='Número exterior',
                            required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder':'Número exterior'
                                }))

    numero_int = forms.CharField(max_length=50,
                            label='Número interior',
                            required=False,
                            widget=forms.TextInput(
                                attrs={'placeholder':'Número interior'
                                }))

'''
