from django.shortcuts import render
from .models import Bem
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render_to_response
import csv
import datetime, json, codecs

def bens_list(request):
	bens = Bem.objects.all()
	return render(request, 'bens/bens_list.html', {'bens': bens})

def detail (request, bens_id):
	bem = get_object_or_404(Bem, pk=bens_id)
	return render(request, 'bens/detail.html', {'bem': bem})
