# Generated by Django 3.0.7 on 2020-07-24 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0003_tipo_estado_equipo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tipo_estado_equipo',
        ),
    ]