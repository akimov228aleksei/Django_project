"""Module containing fields and methods of the model"""

import logging
from django.db import models


logger = logging.getLogger(__name__)


class Department(models.Model):
    """Class containing fields and methods of the model"""

    name = models.CharField('Department:', max_length=30, unique=True)

    @property
    def salary(self):
        """A function that calculates the average salary of each department"""

        from department.DAO import EmployeeDAO

        logger.info("Database query executed (dep_models_salary)")
        emp_set = EmployeeDAO.filter_dep(value=self.pk)
        sal = 0
        if emp_set:
            sal = round(sum([emp.salary for emp in emp_set]) / len(emp_set))

        return sal

    @property
    def amount(self):
        """A function that counts the number of employees in each department"""

        from department.DAO import EmployeeDAO

        logger.info("Database query executed (dep_models_amount)")
        queryset = EmployeeDAO.filter_dep(value=self.pk)

        return len(queryset)

    @staticmethod
    def get_absolute_url():
        """A function that returns an absolute URL"""

        return '/'

    def __str__(self):
        """A function that returns a reference to the name field"""

        return self.name
