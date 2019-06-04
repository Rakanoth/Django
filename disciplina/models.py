from django.db import models

class Disciplina(models.Model):
	nome = models.TextField()
	professor = models.TextField()
	ementa = models.TextField()
	carga_horaria = models.IntegerField()

	
