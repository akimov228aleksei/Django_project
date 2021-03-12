"""Module containing fields and methods of the model"""

from django.db import models


class Department(models.Model):
    """Class containing fields and methods of the model"""

    name = models.CharField('Department:', max_length=30)

    @property
    def salary(self):
        """A function that calculates the average salary of each department"""

        from department.models.employee import Employee

        emp_set = Employee.objects.filter(dep=self.pk)
        sal = 0
        if emp_set:
            sal = round(sum([emp.salary for emp in emp_set]) / len(emp_set))

        return sal

    @property
    def amount(self):
        """A function that counts the number of employees in each department"""

        from department.models.employee import Employee

        emp_set = Employee.objects.filter(dep=self.pk)

        return len(emp_set)

    @staticmethod
    def get_absolute_url():
        """A function that returns an absolute URL"""

        return '/'

    def __str__(self):
        """A function that returns a reference to the name field"""

        return self.name
