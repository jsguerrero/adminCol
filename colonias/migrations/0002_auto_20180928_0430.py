# Generated by Django 2.1 on 2018-09-28 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('colonias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat_direccion_usuario',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='cat_direccion_usuario',
            name='object_id',
        ),
        migrations.AddField(
            model_name='cat_direccion_usuario',
            name='cla_asentamiento',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cat_direccion_usuario',
            name='cla_usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_direccion', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
    ]
