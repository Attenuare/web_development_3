from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
	return render(request, 'home.html')

def christmas(request):
	time = datetime.now()
	christmas = True if time.month == 12 and time.day == 25 else False
	return render(request, 'christmas.html', {'christmas': christmas})

def tiradentes(request):
	time = datetime.now()
	tiradentes = True if time.month == 4 and time.day == 21 else False
	return render(request, 'tiradentes.html', {'tiradentes': tiradentes})
