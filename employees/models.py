from django.db import models

# Create your models here.


class Color(models.Model):
    # id primary key is created automaticly
    name = models.CharField(max_length=200)
    

class Department(models.Model):
    # id primary key is created automaticly
    name = models.CharField(max_length=200)
    

class Employees(models.Model):
    # id primary key is created automaticly
    name           = models.CharField(max_length=200)
    age            = models.IntegerField()
    is_senior      = models.BooleanField(default=True)   # as requested in the wor document
    favorite_color = models.ForeignKey(Color, on_delete=models.CASCADE, default=2) # TODO: change cascade to a better function so it wont delete the object
    Department     = models.ForeignKey(Department, on_delete=models.CASCADE) # TODO: change cascade to a better function so it wont delete the object
    

    

