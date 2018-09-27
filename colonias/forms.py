#from django.contrib.auth.forms import UserCreationForm
#from .models import cat_usuario
from django import forms

class formulario_registro(forms.Form):

    nombre = forms.CharField(max_length=50,
                             label='Nombre',
                             required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':'Nombre(s)'
                                 }))

    apellido_paterno = forms.CharField(max_length=50,
                                       label='Apellido Paterno',
                                       required=True,
                                       widget=forms.TextInput(
                                           attrs={
                                               'placeholder':'Apellido Paterno'
                                           }))

    apellido_materno = forms.CharField(max_length=50,
                                       label='Apellido Materno',
                                       required=False,
                                       widget=forms.TextInput(
                                           attrs={
                                               'placeholder':'Apellido Materno'
                                           }))

    codigo_postal = forms.IntegerField(label='Código Postal',
                                       required=True,
                                       widget=forms.TextInput(
                                           attrs={
                                               'placeholder':'Código Postal',
                                               'onfocusout':'validar_codigo_postal(this)',
                                               'pattern':'(\d{5}?)'
                                           }))

    '''estado = forms.CharField(max_length=50,
                             label='Estado',
                             required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':'Estado',
                                     'readonly':'True'
                                 }))

    municipio = forms.CharField(max_length=50,
                             label='Municipio',
                             required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':'Municipio',
                                     'readonly':'True'
                                 }))'''

    colonia = forms.ChoiceField(label='Colonia',
                                required=True,
                                widget=forms.Select(
                                 attrs={
                                     'required':' True'
                                 }))

    calle = forms.CharField(max_length=50,
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

    correo_electronico1 = forms.EmailField(max_length=100,
                             label='Correo electrónico',
                             required=True,
                             help_text="Correo electrónico",
                             widget=forms.EmailInput(
                                 attrs={
                                     'placeholder':'Correo electrónico'
                                 }))

    #correo_electronico2 = forms.EmailField(max_length=100,
    #                         label='Confirmar correo electrónico',
    #                         required=True,
    #                         help_text="Correo correo electrónico",
    #                         widget=forms.EmailInput(
    #                             attrs={
    #                                 'placeholder':'Confirmar correo electrónico',
    #                                 'required': 'True'
    #                             }))

    contrasena1 = forms.CharField(required=True,
                                  label='Contraseña',
                                  help_text='Mínimo 8 caracteres con mayúscula, minúscula y número o caracter especial',
                                  widget=forms.PasswordInput(
                                      attrs={'id':'contrasena1',
                                             'placeholder':'Contraseña',
                                             'pattern':'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                      }))

    contrasena2 = forms.CharField(required=True,
                                  label='Confirmar contraseña',
                                  help_text='Mínimo 8 caracteres con mayúscula, minúscula y número o caracter especial',
                                  widget=forms.PasswordInput(
                                      attrs={
                                          'placeholder':'Confirmar contraseña',
                                          'pattern':'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$',
                                          'oninput':'validar_contrasena(this)'
                                      }))


    #class Meta:
    #    model = cat_usuario
    #    fields = {'email', 'password1', 'password2'}

    def clean(self):
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
