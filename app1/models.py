from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=40)
    