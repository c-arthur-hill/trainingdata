from django import forms
from .models import FitFile

class FitFileForm(forms.ModelForm):
    uploaded_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = FitFile
        fields = ['uploaded_file']
