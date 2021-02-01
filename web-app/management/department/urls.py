from django.urls import path
from . import views


urlpatterns = [
    path('', views.department_home, name='home'),
    path('add', views.add, name='add'),
    path('<int:pk>/update', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('<int:pk>/delete', views.DepartmentDeleteView.as_view(), name='department-delete')
]
