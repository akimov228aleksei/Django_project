"""Module containing fields and methods of the model"""

from django.db import models
from .employee import Employee


class Vacation(models.Model):
    """Class containing fields and methods of the model"""

    name_vacation = models.ForeignKey(Employee, to_field='name_employee', on_delete=models.CASCADE, unique=True)
    date1 = models.DateField('Date start:')
    date2 = models.DateField('Date end:')

    @staticmethod
    def get_absolute_url():
        """A function that returns an absolute URL"""

        return '/vacation/'

    def __str__(self):
        """A function that returns a reference to the name field"""

        return str(self.name_vacation)
