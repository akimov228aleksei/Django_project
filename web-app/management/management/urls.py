from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('department.department_urls')),
    path('employee/', include('department.employee_urls')),
    path('vacation/', include('department.vacation_urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
