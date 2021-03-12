"""Module containing fields and methods of the model"""

from django.db import models


class Vacation(models.Model):
    """Class containing fields and methods of the model"""

    name = models.CharField('Employee:', max_length=30)
    date1 = models.DateField('Date:', max_length=30)
    date2 = models.DateField('Date:', max_length=30)

    @staticmethod
    def get_absolute_url():
        """A function that returns an absolute URL"""

        return '/vacation/'

    def __str__(self):
        """A function that returns a reference to the name field"""

        return self.name
