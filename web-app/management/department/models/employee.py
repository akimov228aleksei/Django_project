from django.db import models
from .department import Department

class Employee(models.Model):

    name = models.CharField('Employee:', max_length=30)
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.CharField('Salary:', max_length=30)
    position = models.CharField('Position:', max_length=30)
    date = models.DateField('Date:', max_length=30)


    def get_absolute_url(self):
        return '/employee/'

    def __str__(self):
       return self.name