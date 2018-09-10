from django.db import models

# Create your models here.

class CodigoPostal(models.Model):
    """
    Clase que define el model de datos para Codigo Postal
    """

    cla_codigo_postal = models.CharField(max_length=20,
                                         verbose_name="Codigo Postal",
                                         primary_key=True)

    cla_pais = models.ForeignKey('Pais',
                                  on_delete=models.CASCADE)

    cla_estado = models.ForeignKey('Estado',
                                   on_delete=models.CASCADE)

    cla_municipio = models.ForeignKey('Municipio',
                                      on_delete=models.CASCADE)

    cla_colonia = models.ManyToManyField('Colonia')

class Pais(models.Model):
    cla_pais = models.IntegerField(verbose_name='Clave Pais',
                                   primary_key=True)

    nom_pais = models.CharField(max_length=200,
                                verbose_name='Nombre Pais')

    def __str__(self):
        return self.nom_pais

class Estado(models.Model):
    cla_pais = models.ForeignKey('Pais',
                                 on_delete=models.CASCADE)

    cla_estado = models.IntegerField(verbose_name='Clave Estado',
                                     primary_key=True)

    nom_estado = models.CharField(max_length=200,
                                  verbose_name='Nombre Estado')

    def __str__(self):
        return self.nom_estado

class Municipio(models.Model):
    cla_estado = models.ForeignKey('Estado',
                                   on_delete=models.CASCADE)

    cla_municipio = models.IntegerField(verbose_name='Clave Municipio',
                                        primary_key=True)

    nom_municipio = models.CharField(max_length=200,
                                     verbose_name='Nombre Municipio')

    def __str__(self):
        return self.nom_municipio

class Colonia(models.Model):
    cla_codigo_postal = models.ForeignKey('CodigoPostal',
                                          on_delete=models.CASCADE)

    cla_municipio = models.ForeignKey('Municipio',
                                      on_delete=models.CASCADE)

    cla_colonia = models.IntegerField(verbose_name='Clave Colonia',
                                      primary_key=True)

    nom_colonia = models.CharField(max_length=200,
                                   verbose_name='Nombre Colonia')

    def __str__(self):
        return self.nom_colonia
