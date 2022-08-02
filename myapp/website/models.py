from django.db import models

# Create your models here.models
class animal(models.Model):
    name=models.CharField(max_length=100)
