from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    todo = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)