import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diary_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.diary_text
    
