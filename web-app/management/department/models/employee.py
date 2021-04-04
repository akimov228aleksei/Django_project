"""Module containing fields and methods of the model"""

from django.db import models
from .department import Department


class Employee(models.Model):
    """Class containing fields and methods of the model"""

    name_employee = models.CharField('Employee:', unique=True, max_length=30)
    dep = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    salary = models.PositiveIntegerField('Salary:', default=0)
    position = models.CharField('Position:', max_length=30)
    date = models.DateField('Date:')

    @staticmethod
    def get_absolute_url():
        """A function that returns an absolute URL"""

        return '/employee/'

    def __str__(self):
        """A function that returns a reference to the name field"""

        return self.name_employee
