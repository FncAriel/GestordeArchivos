# Generated by Django 2.2.2 on 2019-06-21 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planos', '0002_auto_20190620_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquitecto',
            name='inmobiliarias',
        ),
    ]
