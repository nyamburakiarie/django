from django.db import models


# Create your models here.

class Student(models.Model):
    
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    years_of_practice = models.IntegerField()

    def __str__(self):
        return self.firstname

