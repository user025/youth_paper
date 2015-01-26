from django.db import models

# Create your models here.
class academy(models.Model):
    author=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    keyword=models.CharField(max_length=255)
    url=models.URLField(max_length=255)

class news(models.Model):
    author=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    keyword=models.CharField(max_length=255)
    url=models.URLField(max_length=255)

class life(models.Model):
    author=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    keyword=models.CharField(max_length=255)
    url=models.URLField(max_length=255)

