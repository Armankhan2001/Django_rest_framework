from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField( max_length=50)
    Place = models.CharField( max_length=50)
    City = models.CharField( max_length=50)
