# Generated by Django 3.1.2 on 2020-11-02 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formulario',
            fields=[
                ('id_form', models.AutoField(db_column='id_form', primary_key=True, serialize=False)),
                ('nombres', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(max_length=9, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('comentario', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_usuario', models.AutoField(db_column='id_usuario', primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('rut', models.CharField(max_length=19, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=20, null=True)),
                ('genero', models.CharField(blank=True, max_length=10, null=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['rut'],
            },
        ),
    ]
