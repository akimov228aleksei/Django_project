from django.contrib import admin
from .models.department_models import Department
from .models.employee_models import Employee
from .models.vacation_models import Vacation

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Vacation)