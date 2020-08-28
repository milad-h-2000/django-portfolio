from django.db import models
import datetime


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title
