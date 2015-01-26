from django.db import models

class list(models.Model):
    account=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    
