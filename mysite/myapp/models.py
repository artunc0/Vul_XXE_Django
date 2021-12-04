from django.db import models

# Create your models here.

class Book(moels.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
