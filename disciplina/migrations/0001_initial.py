# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.TextField()),
                ('professor', models.TextField()),
                ('ementa', models.TextField()),
                ('carga_horaria', models.IntegerField()),
            ],
        ),
    ]
