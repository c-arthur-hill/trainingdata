from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model
from .calendars import TrainingData
from .forms import FitFileForm
from .models import FitFile, DailyData
import datetime

class FitFileView(CreateView):
    form_class = FitFileForm
    template_name = 'calendars/upload.html'
    success_url = '/calendar/home/'

    def form_valid(self, form):
        form.instance.user = get_user_model().objects.get(email='foo.bart@bart.com')
        return super(FitFileView, self).form_valid(form)

class CalendarView(ListView):
    model = DailyData
    template_name = 'calendars/calendar.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CalendarView, self).get_context_data(*args, **kwargs)
        now = datetime.datetime.now()
        training_data = TrainingData()
        training_data_html = training_data.formatmonth(now.year, now.month, withyear=True)
        context['training_data_html'] = mark_safe(training_data_html)
        context['fit_files'] = FitFile.objects.all()
        return context
