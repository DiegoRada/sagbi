# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_autor', models.CharField(max_length=50)),
                ('estatus_autor', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_director', models.CharField(max_length=50)),
                ('estatus_director', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_libro', models.CharField(max_length=150)),
                ('isbn', models.CharField(max_length=100, null=True)),
                ('edicion', models.CharField(max_length=100, null=True)),
                ('publicacion', models.CharField(max_length=100, null=True)),
                ('descripcion', models.TextField(max_length=1000, null=True)),
                ('url_libro', models.CharField(max_length=255)),
                ('url_afiche_libro', models.CharField(max_length=255, null=True)),
                ('url_ficha_libro', models.CharField(max_length=255, null=True)),
                ('autor', models.ForeignKey(to='sagbi.Autores')),
            ],
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_pais', models.CharField(unique=True, max_length=50)),
                ('estatus_pais', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_original', models.CharField(max_length=150)),
                ('titulo_traducido', models.CharField(max_length=150, null=True)),
                ('anio', models.PositiveIntegerField()),
                ('duracion', models.CharField(max_length=10)),
                ('guion', models.CharField(max_length=255, null=True)),
                ('fotografia', models.CharField(max_length=255, null=True)),
                ('reparto', models.CharField(max_length=255, null=True)),
                ('productora', models.CharField(max_length=150, null=True)),
                ('sinopsis', models.TextField(max_length=800, null=True)),
                ('criticas', models.TextField(max_length=1300, null=True)),
                ('url_pelicula', models.CharField(max_length=255)),
                ('url_afiche_pelicula', models.CharField(max_length=255, null=True)),
                ('url_subtitulo', models.CharField(max_length=255, null=True)),
                ('url_ficha_pelicula', models.CharField(max_length=255, null=True)),
                ('director', models.ForeignKey(to='sagbi.Directores')),
                ('pais', models.ForeignKey(to='sagbi.Paises')),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion_libros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valoracion_libro', models.PositiveIntegerField()),
                ('id_libro', models.ForeignKey(to='sagbi.Libros')),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion_peliculas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valoracion_pelicula', models.PositiveIntegerField()),
                ('id_pelicula', models.ForeignKey(to='sagbi.Peliculas')),
            ],
        ),
    ]
