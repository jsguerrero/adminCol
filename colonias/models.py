from django.db import models

# Create your models here.

class cat_codigo_postal(models.Model):
    """
    Clase que define el model de datos para Codigo Postal
    """

    cla_codigo_postal = models.CharField(max_length=20,
                                         verbose_name="Codigo Postal",
                                         primary_key=True)

    cla_pais = models.ForeignKey('cat_pais',
                                  on_delete=models.CASCADE)

    cla_estado = models.ForeignKey('cat_estado',
                                   on_delete=models.CASCADE)

    cla_municipio = models.ForeignKey('cat_municipio',
                                      on_delete=models.CASCADE)

    #cla_asentamiento = models.ForeignKey('cat_asentamiento',
    #                                     on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cla_codigo_postal', 'cla_pais', 'cla_estado', 'cla_municipio')

    def __str__(self):
        return self.cla_codigo_postal

class cat_pais(models.Model):
    cla_pais = models.IntegerField(verbose_name='Clave Pais',
                                   primary_key=True)

    nom_pais = models.CharField(max_length=200,
                                verbose_name='Nombre Pais')

    def __str__(self):
        return self.nom_pais

class cat_estado(models.Model):
    cla_pais = models.ForeignKey('cat_pais',
                                 on_delete=models.CASCADE)

    cla_estado = models.IntegerField(verbose_name='Clave Estado')

    nom_estado = models.CharField(max_length=200,
                                  verbose_name='Nombre Estado')

    class Meta:
        unique_together = ('cla_pais', 'cla_estado')

    def __str__(self):
        return self.nom_estado

class cat_municipio(models.Model):
    cla_pais = models.ForeignKey('cat_pais',
                                 on_delete=models.CASCADE)

    cla_estado = models.ForeignKey('cat_estado',
                                   on_delete=models.CASCADE)

    cla_municipio = models.IntegerField(verbose_name='Clave Municipio')

    nom_municipio = models.CharField(max_length=200,
                                     verbose_name='Nombre Municipio')

    class Meta:
        unique_together = ('cla_pais', 'cla_estado', 'cla_municipio')

    def __str__(self):
        return self.nom_municipio

class cat_asentamiento(models.Model):
    cla_codigo_postal = models.ForeignKey('cat_codigo_postal',
                                          on_delete=models.CASCADE)

    #cla_pais = models.ForeignKey('cat_pais',
    #                             on_delete=models.CASCADE)

    #cla_estado = models.ForeignKey('cat_estado',
    #                               on_delete=models.CASCADE)

    #cla_municipio = models.ForeignKey('cat_municipio',
    #                                  on_delete=models.CASCADE)

    cla_tipo_asentamiento = models.ForeignKey('cat_tipo_asentamiento',
                                              on_delete=models.CASCADE)

    cla_asentamiento = models.IntegerField(verbose_name='Clave Asentamiento')

    nom_asentamiento = models.CharField(max_length=200,
                                   verbose_name='Nombre Colonia')

    class Meta:
        #unique_together = ('cla_codigo_postal', 'cla_pais', 'cla_estado', 'cla_municipio', 'cla_asentamiento')
        unique_together = ('cla_codigo_postal', 'cla_asentamiento')

    def __str__(self):
        return self.nom_asentamiento

class cat_tipo_asentamiento(models.Model):
    cla_tipo_asentamiento = models.IntegerField(verbose_name='Clave Tipo Asentamiento',
                                                primary_key=True)

    nom_tipo_asentamiento = models.CharField(verbose_name='Nombre Tipo Asentamiento',
                                             max_length=200)

    def __str__(self):
        return self.nom_tipo_asentamiento

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class cat_usuario_manager(BaseUserManager):
    """"
    Modelo para manejar modelo User sin usar el campo username
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Crear y guardar usuario con correo y contrasena
        """
        if not email:
            raise ValueError('Es necesario el correo electrónico')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Crear y guardar usuario regular con correo y contrasena
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Crear y guardar un Super usuario con correo y contrasena
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El super usuario debe tener is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El super usuario debe tener is_superuser=True')

        return self._create_user(email, password, **extra_fields)

class cat_usuario(AbstractUser):
    username = None

    email = models.EmailField(_('Correo electrónico'),
                              unique=True)

    nom_usuario = models.CharField(verbose_name='Nombre(s)',
                                   max_length=200)

    apellido_paterno = models.CharField(verbose_name='Apellido Paterno',
                                        max_length=200)

    apellido_materno = models.CharField(verbose_name='Apellido Materno',
                                        max_length=200,
                                        null=True)

    es_admin = models.BooleanField(verbose_name='Administrador',
                                   default=False)

    es_guardia = models.BooleanField(verbose_name='Guardia',
                                     default=False)

    cla_asentamiento = models.ManyToManyField('cat_direccion_usuario',
                                              verbose_name='Colonias a las que pertenece')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nom_usuario', 'apellido_paterno']

    objects = cat_usuario_manager()

    def get_es_guardia(self):
        perfil_guardia = None
        if hasattr(self, 'perfil_guardia'):
            perfil_guardia = self.perfil_guardia
        return perfil_guardia

    def get_es_admin(self):
        perfil_admin = None
        if hasattr(self, 'perfil_admin'):
            perfil_admin = self.perfil_admin
        return perfil_admin

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class cat_direccion_usuario(models.Model):
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     related_name='content_type_direccion')

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    #cla_usuario = models.ForeignKey('cat_usuario',
    #                                verbose_name='Clave Usuario',
    #                                on_delete=models.CASCADE)

    #cla_codigo_postal= models.ForeignKey('cat_codigo_postal',
    #                                     on_delete=models.CASCADE)

    #cla_asentamiento = models.ForeignKey('cat_asentamiento',
    #                                     on_delete=models.CASCADE,
    #                                     verbose_name='Clave Asentamiento')

    nom_calle = models.CharField(verbose_name='Calle',
                                 max_length=200)

    num_exterior = models.IntegerField(verbose_name='Numero Exterior')

    num_interior = models.CharField(verbose_name='Interior',
                                  blank=True,
                                  max_length=200)

class perfil_guardia(models.Model):
    cla_usuario = models.OneToOneField('cat_usuario',
                                   on_delete=models.CASCADE)

    cla_asentamiento = models.OneToOneField('cat_asentamiento',
                                            on_delete=models.CASCADE)

    activo = models.BooleanField(default=True)

class perfil_admin(models.Model):
    cla_usuario = models.OneToOneField('cat_usuario',
                                   on_delete=models.CASCADE)

    cla_asentamiento = models.OneToOneField('cat_asentamiento',
                                            on_delete=models.CASCADE)

    activo = models.BooleanField(default=True)
