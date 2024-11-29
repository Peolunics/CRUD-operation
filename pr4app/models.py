from typing import Any
from django.db import models

# Create your models here.
class phonebook(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=10)