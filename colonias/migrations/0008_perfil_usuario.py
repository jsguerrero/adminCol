# Generated by Django 2.1 on 2018-10-02 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('colonias', '0007_remove_cat_usuario_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil_usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llave_activacion', models.CharField(blank=True, max_length=40)),
                ('expiracion_llave', models.DateTimeField(default=django.utils.timezone.now)),
                ('cla_usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
