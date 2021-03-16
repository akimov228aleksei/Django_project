"""Package initialization"""

from .department import department_home, add, DepartmentUpdateView, DepartmentDeleteView
from .employee import employee_add, employee_home, EmployeeUpdateView, EmployeeDeleteView
from .vacation import vacation_home, vacation_add, VacationUpdateView, VacationDeleteView
