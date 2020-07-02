from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Student(models.Model):

    admission = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'student_data'

class Result(models.Model):

    admission = models.ForeignKey(Student, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=50)
    maths = models.IntegerField()
    english = models.IntegerField()
    hindi = models.IntegerField()       
    science = models.IntegerField()
    
    class Meta:
        managed = True
        db_table = 'result_data'


            