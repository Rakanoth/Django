from django.shortcuts import render
from .models import Candidato
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import CandidatoForm
from django.shortcuts import redirect
from django.shortcuts import render_to_response
import csv
import datetime, json, codecs

def candidatos_list(request):
    candidatos = Candidato.objects.all()
    return render(request, 'candidato/candidatos_list.html', {'candidatos': candidatos})

def detail (request, candidato_id):
	candidato = get_object_or_404(Candidato, pk=candidato_id)
	return render(request, 'candidato/detail.html', {'candidato': candidato})

def candidato_new(request):
    if request.method == "POST":
        form = CandidatoForm(request.POST)
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.save()
            return redirect('candidato.views.candidatos_list')
    else:
        form = CandidatoForm()
    return render(request, 'candidato/candidato_edit.html', {'form': form})

def candidato_edit(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method == "POST":
        form = CandidatoForm(request.POST, instance=candidato)
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.save()
            return redirect('candidato.views.candidatos_list')
    else:
        form = CandidatoForm(instance=candidato)
    return render(request, 'candidato/candidato_edit.html', {'form': form})