from django.db import models

# Create your models here.
class Student(models.Model):
    # f_name = models.CharField( max_length=50)
    # l_name = models.CharField(max_length = 50)
    roll_no = models.IntegerField()
    full_name = models.CharField(max_length=100)