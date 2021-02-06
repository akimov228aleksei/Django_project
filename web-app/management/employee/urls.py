from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_home, name='employee_home'),
    path('add', views.add, name='employee_add'),
    path('<int:pk>/update', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('<int:pk>/delete', views.EmployeeDeleteView.as_view(), name='employee-delete')

]