from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model

class EmailView(CreateView):
    model = get_user_model()
    fields = ['email', 'password']
    success_url = '/calendar/view/today/'

    def get_form(self, form_class=None):
        form = super(EmailView, self).get_form(form_class)
        form.fields['email'].widget = forms.EmailInput(attrs={'class': "col-9 col-xl-4"})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class': "col-9 col-xl-4"})
        return form
