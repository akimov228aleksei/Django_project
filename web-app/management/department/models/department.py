from django.db import models

class Department(models.Model):

    name = models.CharField('Department:', max_length=30)



    def get_absolute_url(self):
        return '/'

    def __str__(self):
       return self.name