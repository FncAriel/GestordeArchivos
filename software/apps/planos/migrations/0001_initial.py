# Generated by Django 2.2.2 on 2019-06-20 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='anotacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.SmallIntegerField()),
                ('y', models.SmallIntegerField()),
                ('detalle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='arquitecto',
            fields=[
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=254, primary_key=True, serialize=False)),
                ('telefono', models.BigIntegerField(default='0')),
                ('inmobiliarias', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('u', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.BigIntegerField()),
                ('inmobiliaria', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='jefeDeTaller',
            fields=[
                ('u', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='')),
                ('especificacion', models.TextField(null=True)),
                ('ultima_carga', models.DateField()),
                ('arquitecto', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='planos.arquitecto')),
            ],
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmobiliaria', models.TextField(null=True)),
                ('proyecto_inmobiliario', models.TextField(null=True)),
                ('entrega_total', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='render',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='')),
                ('finalizado', models.BooleanField(default=False)),
                ('plano', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planos.plano')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planos.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iteracion', models.SmallIntegerField()),
                ('render', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='planos.render')),
            ],
        ),
        migrations.CreateModel(
            name='referencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='')),
                ('especificacion', models.FileField(upload_to='')),
                ('detalle', models.TextField()),
                ('plano', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='planos.plano')),
            ],
        ),
        migrations.CreateModel(
            name='modelador',
            fields=[
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=254, primary_key=True, serialize=False)),
                ('telefono', models.BigIntegerField(default='0')),
                ('activo', models.BooleanField()),
                ('jefe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='planos.jefeDeTaller')),
            ],
        ),
        migrations.CreateModel(
            name='horasHombre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('termino', models.DateField()),
                ('productos', models.TextField()),
                ('modelador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='planos.modelador')),
            ],
        ),
        migrations.CreateModel(
            name='hito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('producto', models.TextField(null=True)),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planos.proyecto')),
            ],
        ),
    ]
