from django.db import models

class academy(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    author=models.CharField(max_length=255)
    field=models.CharField(max_length=255)
    keyword=models.CharField(max_length=255)
    issue=models.IntegerField() 
    article=models.FileField(upload_to='academy/')

class news(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    author=models.CharField(max_length=255)
    keyword=models.CharField(max_length=255)
    issue=models.IntegerField()
    article=models.FileField(upload_to='news/')


class overseas(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    author=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    keyword=models.CharField(max_length=255)
    issue=models.IntegerField()
    article=models.FileField(upload_to='overseas/')

