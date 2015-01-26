from django.db import models

class user(models.Model):
    email=models.CharField(max_length=255)
    keyword=models.CharField(max_length=255)
    type=models.CharField(max_length=255)

class keywords(models.Model):
    keyword=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    
