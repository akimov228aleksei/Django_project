"""Module containing fields and methods of the model"""

from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from .department import Department


class Employee(models.Model):
    """Class containing fields and methods of the model"""

    def no_future(value):
        if value > date.today():
            raise ValidationError('Date cannot be in the future.')

    name = models.CharField('Employee:', max_length=30)
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField('Salary:')
    position = models.CharField('Position:', max_length=30)
    date = models.DateField(validators=[no_future])

    @staticmethod
    def get_absolute_url():
        """A function that returns an absolute URL"""

        return '/employee/'

    def __str__(self):
        """A function that returns a reference to the name field"""

        return self.name
