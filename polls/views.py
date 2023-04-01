from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from datetime import date

def index(request):
	return render(request, 'home.html')

def calculate_days(f_day: int, f_month: int) -> int:
	today = datetime.now()
	f_date = date(today.year, f_month, f_day)
	s_date = date(today.year, today.month, today.day)
	return f_date - s_date

def christmas(request):
	time = datetime.now()
	lasting = 0
	christmas = True if time.month == 12 and time.day == 25 else False
	if not christmas:
		lasting = calculate_days(25, 12)
	return render(request, 'christmas.html', {'christmas': christmas, 'lasting': lasting.days})

def tiradentes(request):
	time = datetime.now()
	lasting = 0
	tiradentes = True if time.month == 4 and time.day == 21 else False
	if not tiradentes:
		lasting = calculate_days(21, 4)
	return render(request, 'tiradentes.html', {'tiradentes': tiradentes, 'lasting': lasting.days})
