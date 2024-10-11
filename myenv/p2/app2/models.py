from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    location=models.CharField(max_length=50)
    