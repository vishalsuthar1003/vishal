from django.db import models

# Create your models here

# class Teacher(models.Model):
#     Firstname = models.CharField(max_length=50)
#     Lastname = models.CharField(max_length=50)
#     Course = models.CharField(max_length=50)
    
# class Student(models.Model):
#     teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
#     Firstname = models.CharField(max_length=50)
#     Lastname = models.CharField(max_length=50)
#     Address = models.CharField(max_length=50)

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailFeild(max_length=50)
    password = models.CharField(max_length=50)