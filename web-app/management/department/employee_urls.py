from django.urls import path
from .views.employee_views import *


urlpatterns = [
    path('', employee_home, name='employee_home'),
    path('add', add, name='employee_add'),
    path('<int:pk>/update', EmployeeUpdateView.as_view(), name='employee-update'),
    path('<int:pk>/delete', EmployeeDeleteView.as_view(), name='employee-delete')

]