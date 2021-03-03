from django.db import models


class Department(models.Model):

    name = models.CharField('Department:', max_length=30)

    @property
    def salary(self):

        from department.models.employee import Employee

        average = 1
        count = 1
        emp_set = Employee.objects.filter(dep__startswith='Front')

        for i in emp_set:
            average += int(i.salary[:1])
            count += 1
            average = average / count

        return average



    def get_absolute_url(self):
        return '/'

    def __str__(self):
       return self.name