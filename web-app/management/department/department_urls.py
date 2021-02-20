from django.urls import path
from .views.department_views import *


urlpatterns = [
    path('', department_home, name='home'),
    path('add', add, name='add'),
    path('<int:pk>/update', DepartmentUpdateView.as_view(), name='department-update'),
    path('<int:pk>/delete', DepartmentDeleteView.as_view(), name='department-delete')
]
