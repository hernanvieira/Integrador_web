# Generated by Django 3.0.7 on 2020-07-24 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_delete_tipo_estado_equipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_estado_equipo',
            fields=[
                ('id_tipo_estado_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='nombre_estado')),
            ],
        ),
    ]