"""Module with API URL ratios"""

from django.urls import path
from department.api.views import department, employee, vacation


urlpatterns = [
    path('department/create', department.DepartmentCreateView.as_view(), name='department-api-create'),
    path('department/list', department.DepartmentListView.as_view(), name='department-api-list'),
    path('department/detail/<int:pk>/', department.DepartmentDetailView.as_view(), name='department-api-detail'),
    path('employee/create', employee.EmployeeCreateView.as_view()),
    path('employee/list', employee.EmployeeListView.as_view()),
    path('employee/detail/<int:pk>/', employee.EmployeeDetailView.as_view()),
    path('vacation/create', vacation.VacationCreateView.as_view()),
    path('vacation/list', vacation.VacationListView.as_view()),
    path('vacation/detail/<int:pk>/', vacation.VacationDetailView.as_view())
]
