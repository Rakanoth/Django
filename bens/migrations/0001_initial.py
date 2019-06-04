# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('data_geracao', models.DateField()),
                ('hora_geracao', models.TimeField()),
                ('ano_eleicao', models.IntegerField()),
                ('descricao_eleicao', models.CharField(max_length=100)),
                ('sigla_uf', models.CharField(max_length=2)),
                ('sequencial_candidato', models.IntegerField()),
                ('cd_tipo_bem_candidato', models.IntegerField()),
                ('ds_tipo_bem_candidato', models.TextField()),
                ('detalhe_bem', models.TextField()),
                ('valor_bem', models.DecimalField(max_digits=16, decimal_places=3)),
                ('data_ultima_att', models.DateField()),
                ('hora_ultima_att', models.TimeField()),
            ],
        ),
    ]
