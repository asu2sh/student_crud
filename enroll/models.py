from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=32)