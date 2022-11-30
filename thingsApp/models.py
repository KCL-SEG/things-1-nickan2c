from django.db import models

# Create your models here.

class Thing(models.Model):
    # name must be unique, must not be blank, and must consist of 30 characters or less.
    name = models.CharField(max_length=30, unique=True, blank=False)
    # description must not be blank, and must consist of 100 characters or less.
    description = models.CharField(max_length=100, blank=False)
    quanitity = models.IntegerField(min_value=0, max_value=100)