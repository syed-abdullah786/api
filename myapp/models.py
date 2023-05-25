from django.db import models

# Create your models here.
class Items(models.Model):
    text = models.CharField(max_length=200)