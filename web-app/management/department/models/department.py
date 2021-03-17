"""Module containing fields and methods of the model"""

from django.db import models
from django.core.exceptions import ValidationError


class Department(models.Model):
    """Class containing fields and methods of the model"""

    def checking_name(value):
        """check for duplicate department name"""

        if Department.objects.filter(name=value):
            raise ValidationError('Such a department already exists.')

    name = models.CharField('Department:', max_length=30, validators=[checking_name])

    @property
    def salary(self):
        """A function that calculates the average salary of each department"""

        from department.models import Employee
        emp_set = Employee.objects.filter(dep=self.pk)
        sal = 0
        if emp_set:
            sal = round(sum([emp.salary for emp in emp_set]) / len(emp_set))

        return sal

    @property
    def amount(self):
        """A function that counts the number of employees in each department"""

        from department.models import Employee

        return len(Employee.objects.filter(dep=self.pk))

    @staticmethod
    def get_absolute_url():
        """A function that returns an absolute URL"""

        return '/'

    def __str__(self):
        """A function that returns a reference to the name field"""

        return self.name
