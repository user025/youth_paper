from django.db import models

# Create your models here.
class list(models.Model):
    keyword=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
