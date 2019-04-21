from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from .calendars import TrainingData
from .forms import FitFileForm
from .models import FitFile
import datetime

class FitFileView(CreateView):
    form_class = FitFileForm
    template_name = 'calendars/training_data.html'
    success_url = '/calendar/home/'

    def form_valid(self, form):
        form.instance.user = get_user_model().objects.get(email='foo.bart@bart.com')
        return super(FitFileView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(FitFileView, self).get_context_data(*args, **kwargs)
        now = datetime.datetime.now()
        training_data = TrainingData()
        training_data_html = training_data.formatmonth(now.year, now.month, withyear=True)
        context['training_data_html'] = mark_safe(training_data_html)
        context['fit_files'] = FitFile.objects.all()
        print(context['fit_files'][0])
        return context
