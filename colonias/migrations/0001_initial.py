# Generated by Django 2.1 on 2018-09-15 00:24

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='cat_usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nom_usuario', models.CharField(max_length=200, verbose_name='Nombre de Usuario')),
                ('apellido_paterno', models.CharField(max_length=200, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=200, verbose_name='Apellido Materno')),
                ('es_admin', models.BooleanField(default=False)),
                ('es_guardia', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='cat_asentamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cla_asentamiento', models.IntegerField(verbose_name='Clave Asentamiento')),
                ('nom_asentamiento', models.CharField(max_length=200, verbose_name='Nombre Colonia')),
            ],
        ),
        migrations.CreateModel(
            name='cat_codigo_postal',
            fields=[
                ('cla_codigo_postal', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Codigo Postal')),
            ],
        ),
        migrations.CreateModel(
            name='cat_estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cla_estado', models.IntegerField(verbose_name='Clave Estado')),
                ('nom_estado', models.CharField(max_length=200, verbose_name='Nombre Estado')),
            ],
        ),
        migrations.CreateModel(
            name='cat_municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cla_municipio', models.IntegerField(verbose_name='Clave Municipio')),
                ('nom_municipio', models.CharField(max_length=200, verbose_name='Nombre Municipio')),
                ('cla_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_estado')),
            ],
        ),
        migrations.CreateModel(
            name='cat_pais',
            fields=[
                ('cla_pais', models.IntegerField(primary_key=True, serialize=False, verbose_name='Clave Pais')),
                ('nom_pais', models.CharField(max_length=200, verbose_name='Nombre Pais')),
            ],
        ),
        migrations.CreateModel(
            name='cat_tipo_asentamiento',
            fields=[
                ('cla_tipo_asentamiento', models.IntegerField(primary_key=True, serialize=False, verbose_name='Clave Tipo Asentamiento')),
                ('nom_tipo_asentimiento', models.CharField(max_length=200, verbose_name='Nombre Tipo Asentamiento')),
            ],
        ),
        migrations.AddField(
            model_name='cat_municipio',
            name='cla_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_pais'),
        ),
        migrations.AddField(
            model_name='cat_estado',
            name='cla_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_pais'),
        ),
        migrations.AddField(
            model_name='cat_codigo_postal',
            name='cla_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_estado'),
        ),
        migrations.AddField(
            model_name='cat_codigo_postal',
            name='cla_municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_municipio'),
        ),
        migrations.AddField(
            model_name='cat_codigo_postal',
            name='cla_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_pais'),
        ),
        migrations.AddField(
            model_name='cat_asentamiento',
            name='cla_codigo_postal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_codigo_postal'),
        ),
        migrations.AddField(
            model_name='cat_asentamiento',
            name='cla_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_estado'),
        ),
        migrations.AddField(
            model_name='cat_asentamiento',
            name='cla_municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_municipio'),
        ),
        migrations.AddField(
            model_name='cat_asentamiento',
            name='cla_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_pais'),
        ),
        migrations.AddField(
            model_name='cat_asentamiento',
            name='cla_tipo_asentamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonias.cat_tipo_asentamiento'),
        ),
        migrations.AlterUniqueTogether(
            name='cat_municipio',
            unique_together={('cla_pais', 'cla_estado', 'cla_municipio')},
        ),
        migrations.AlterUniqueTogether(
            name='cat_estado',
            unique_together={('cla_pais', 'cla_estado')},
        ),
        migrations.AlterUniqueTogether(
            name='cat_codigo_postal',
            unique_together={('cla_codigo_postal', 'cla_pais', 'cla_estado', 'cla_municipio')},
        ),
        migrations.AlterUniqueTogether(
            name='cat_asentamiento',
            unique_together={('cla_codigo_postal', 'cla_pais', 'cla_estado', 'cla_municipio', 'cla_asentamiento')},
        ),
    ]
