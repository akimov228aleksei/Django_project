"""The module contains information that will be presented in the admin panel"""

from django.contrib import admin
from department.models.department import Department
from department.models.employee import Employee
from department.models.vacation import Vacation

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Vacation)
