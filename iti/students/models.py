from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    grade = models.IntegerField(null=True)
