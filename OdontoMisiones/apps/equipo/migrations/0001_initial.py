# Generated by Django 3.0.7 on 2020-07-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(blank=True, max_length=100, null=True, verbose_name='marca')),
                ('modelo', models.CharField(blank=True, max_length=100, null=True, verbose_name='modelo')),
                ('fecha_garantia', models.DateField(blank=True, null=True, verbose_name='fecha_garantia')),
                ('numero_serie', models.PositiveIntegerField(blank=True, null=True, verbose_name='numero_serie')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='observaciones')),
            ],
        ),
        migrations.CreateModel(
            name='estado_equipo',
            fields=[
                ('id_estado_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_estado_equipo', models.DateField(blank=True, null=True, verbose_name='fecha_estado_equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_estado_equipo',
            fields=[
                ('id_tipo_estado_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='nombre_estado')),
            ],
        ),
    ]
