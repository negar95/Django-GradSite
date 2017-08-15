from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    date = models.DateTimeField(default= timezone.now())