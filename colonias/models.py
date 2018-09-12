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

    cla_pais = models.ForeignKey('cat_pais',
                                 on_delete=models.CASCADE)

    cla_estado = models.ForeignKey('cat_estado',
                                   on_delete=models.CASCADE)

    cla_municipio = models.ForeignKey('cat_municipio',
                                      on_delete=models.CASCADE)

    cla_tipo_asentamiento = models.ForeignKey('cat_tipo_asentamiento',
                                              on_delete=models.CASCADE)

    cla_asentamiento = models.IntegerField(verbose_name='Clave Asentamiento')

    nom_asentamiento = models.CharField(max_length=200,
                                   verbose_name='Nombre Colonia')

    class Meta:
        unique_together = ('cla_codigo_postal', 'cla_pais', 'cla_estado', 'cla_municipio', 'cla_asentamiento')

    def __str__(self):
        return self.nom_asentamiento

class cat_tipo_asentamiento(models.Model):
    cla_tipo_asentamiento = models.IntegerField(verbose_name='Clave Tipo Asentamiento',
                                                primary_key=True)

    nom_tipo_asentimiento = models.CharField(verbose_name='Nombre Tipo Asentamiento',
                                             max_length=200)

    def __str__(self):
        return self.nom_tipo_asentamiento

