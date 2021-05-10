"""Module with URL ratios"""

from django.urls import path
from department import views


urlpatterns = [
    path('', views.DepartmentHome.as_view(), name='home'),
    path('add', views.DepartmentAdd.as_view(), name='add'),
    path('<int:pk>/update', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('<int:pk>/delete', views.DepartmentDeleteView.as_view(), name='department-delete'),
    path('employee/', views.EmployeeHome.as_view(), name='employee_home'),
    path('employee/add', views.EmployeeAdd.as_view(), name='employee_add'),
    path('employee/<int:pk>/update', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('vacation/', views.VacationHome.as_view(), name='vacation_home'),
    path('vacation/add', views.VacationAdd.as_view(), name='vacation_add'),
    path('vacation/<int:pk>/update', views.VacationUpdateView.as_view(), name='vacation-update'),
    path('vacation/<int:pk>/delete', views.VacationDeleteView.as_view(), name='vacation-delete'),
]
