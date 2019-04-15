from django.shortcuts import render
from django.utils.safestring import mark_safe
from .calendars import TrainingData
import datetime

def today(request):
    context = {}
    now = datetime.datetime.now()
    training_data = TrainingData()
    training_data_html = training_data.formatmonth(now.year, now.month, withyear=True)
    context['training_data_html'] = mark_safe(training_data_html)
    return render(request, 'calendars/training_data.html', context)
