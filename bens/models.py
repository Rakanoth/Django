from django.db import models

class Bem (models.Model):
	data_geracao = models.DateField()
	hora_geracao = models.TimeField()
	ano_eleicao = models.IntegerField()
	descricao_eleicao = models.CharField(max_length=100)
	sigla_uf = models.CharField(max_length=2)
	sequencial_candidato = models.IntegerField()
	cd_tipo_bem_candidato = models.IntegerField()
	ds_tipo_bem_candidato = models.TextField()
	detalhe_bem = models.TextField()
	valor_bem = models.DecimalField(decimal_places=3, max_digits=16)
	data_ultima_att = models.DateField()
	hora_ultima_att = models.TimeField()