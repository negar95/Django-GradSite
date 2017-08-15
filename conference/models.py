from django.db import models

# Create your models here.

class Conference (models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    date = models.DateField()
    ticket_price = models.IntegerField()
    location = models.CharField(max_length= 1000)
