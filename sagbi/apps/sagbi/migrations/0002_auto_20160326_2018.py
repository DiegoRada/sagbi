# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagbi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='titulo_libro',
            field=models.CharField(max_length=150, db_index=True),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='titulo_original',
            field=models.CharField(max_length=150, db_index=True),
        ),
    ]
