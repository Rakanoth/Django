# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='descricao_cargo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='descricao_grau_instrucao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='despesa_max_campanha',
            field=models.DecimalField(max_digits=16, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='nome_partido',
            field=models.CharField(max_length=100),
        ),
    ]
