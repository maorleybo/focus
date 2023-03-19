from django.db import models

# Create your models here.


class Color(models.Model):
    # id primary key is created automaticly
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    #change the default table name to the one in the word document
    class Meta:
        db_table = "Color"
    

class Department(models.Model):
    # id primary key is created automaticly
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    #change the default table name to the one in the word document
    class Meta:
        db_table = "Department"
    

class Employees(models.Model):
    #TODO: check why the sql command doesnt write it as foreignkey
    # id primary key is created automaticly
    name           = models.CharField(max_length=200)
    age            = models.IntegerField()
    is_senior      = models.BooleanField(default=True)   # as requested in the wor document
    favorite_color = models.ForeignKey(Color, on_delete=models.CASCADE, default=2, db_column='favorite_color') # TODO: change cascade to a better function so it wont delete the object
    department     = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='department'
                                        , default=None) # TODO: change cascade to a better function so it wont delete the object
    
    def __str__(self):
        return self.name
    

    # def __repr__(self):
    #     return self.name

    #change the default table name to the one in the word document
    class Meta:
        db_table = "Employees"

    

