from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from fitparse import FitFile as FitParseFile, FitParseError

class FitFile(models.Model):
    uploaded_file = models.FileField(upload_to='fit_file_uploads/%Y/%m/%d/%M/%S', validators=[FileExtensionValidator(allowed_extensions=['fit'])])
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    # could refactor into signal, but TODO
    def save(self, *args, **kwargs):
        super(FitFile, self).save(*args, **kwargs)
        fit_file = FitParseFile(str(self.uploaded_file.path))
        for record in fit_file.get_messages('record'):
            for record_data in record:
                print(record_data)

class DailyData(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    day = models.DateField()
    miles = models.IntegerField(default=0)
    time = models.TimeField()
    created_at = models.DateTimeField()
