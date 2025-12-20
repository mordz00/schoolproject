from django.db import models
from datetime import date

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}, {self.age}, {self.course}, {self.created_at}"