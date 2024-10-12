# models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
