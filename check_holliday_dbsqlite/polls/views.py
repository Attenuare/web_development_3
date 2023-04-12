from django.http import HttpResponse
from django.shortcuts import render
from .models import HollidayModel
from datetime import datetime

def check_holliday(date: datetime.date) -> dict:
    hollidays = HollidayModel.objects.all()
    possible_holliday = hollidays.filter(day=date.day, month=date.month)
    all_results = list()
    if len(possible_holliday) > 0:
        for holliday in possible_holliday:
            occurrence = {
                "description": holliday.description,
                "country": holliday.country,
                "month": holliday.month,
                "day": holliday.day,
                "flag": holliday.flag
            }
            all_results.append(occurrence)
        return {"all_results": all_results}
    return {"all_results": {}}


def index(request) -> render:
    date = request.GET.get("holliday")
    if date:
        final_date = datetime.strptime(date, '%Y-%m-%d').date()
        if final_date.day == 1 and final_date.month == 1:
            final_date = datetime.now()
    else: 
        final_date = datetime.now()
    hollidays = check_holliday(final_date)
    hollidays['date'] = final_date
    return render(request, "index.html", hollidays)
