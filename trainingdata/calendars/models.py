from django.db import models
from django.contrib.auth import get_user_model

class DailyData(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    day = models.DateField()
    miles = models.IntegerField(default=0)
    time = models.TimeField()
    created_at = models.DateTimeField()
