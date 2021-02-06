from django.urls import path
from . import views


urlpatterns = [
    path('', views.vacation_home, name='vacation_home'),
    path('add', views.add, name='vacation_add'),
    path('<int:pk>/update', views.VacationUpdateView.as_view(), name='vacation-update'),
    path('<int:pk>/delete', views.VacationDeleteView.as_view(), name='vacation-delete')

]