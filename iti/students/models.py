from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    # null=True --> db --/// blank=True--> admin
    email = models.EmailField(max_length=200, unique=True, null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='students/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name