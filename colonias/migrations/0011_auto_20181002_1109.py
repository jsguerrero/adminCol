# Generated by Django 2.1 on 2018-10-02 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colonias', '0010_auto_20181002_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat_direccion_usuario',
            name='cla_asentamiento',
        ),
        migrations.RemoveField(
            model_name='cat_direccion_usuario',
            name='cla_usuario',
        ),
        migrations.RemoveField(
            model_name='cat_usuario',
            name='cla_asentamiento',
        ),
        migrations.RemoveField(
            model_name='perfil_admin',
            name='cla_asentamiento',
        ),
        migrations.RemoveField(
            model_name='perfil_admin',
            name='cla_usuario',
        ),
        migrations.RemoveField(
            model_name='perfil_guardia',
            name='cla_asentamiento',
        ),
        migrations.RemoveField(
            model_name='perfil_guardia',
            name='cla_usuario',
        ),
        migrations.AddField(
            model_name='perfil_admin',
            name='cla_direccion',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='colonias.perfil_vecino'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil_guardia',
            name='cla_direccion',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='colonias.perfil_vecino'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfil_vecino',
            name='activo',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='cat_direccion_usuario',
        ),
    ]
