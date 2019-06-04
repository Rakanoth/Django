from django.shortcuts import render
from .models import Disciplina
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render_to_response
import csv

def disciplinas_list(request):
	materias = Disciplina.objects.all()
	return render(request, 'disciplina/disciplinas_list.html', {'materias': materias})

def detail(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    return render(request, 'disciplina/detail.html', {'disciplina': disciplina})