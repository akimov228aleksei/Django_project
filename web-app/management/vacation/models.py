from django.db import models

class Vacation(models.Model):

    name = models.CharField('Employee:', max_length=30)
    date1 = models.DateField('Date:', max_length=30)
    date2 = models.DateField('Date:', max_length=30)


    def get_absolute_url(self):
        return '/vacation/'

    def __str__(self):
       return self.name