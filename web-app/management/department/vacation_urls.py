from django.urls import path
from .views.vacation_views import *


urlpatterns = [
    path('', vacation_home, name='vacation_home'),
    path('add', add, name='vacation_add'),
    path('<int:pk>/update', VacationUpdateView.as_view(), name='vacation-update'),
    path('<int:pk>/delete', VacationDeleteView.as_view(), name='vacation-delete')

]