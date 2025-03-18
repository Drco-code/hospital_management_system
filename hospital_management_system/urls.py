"""
URL configuration for hospital_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
# Documentation

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),


    path('admin/', admin.site.urls),


    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path('patients/', include('patients.urls')),
    path("medical-history/", include('medical_history.urls')),
    path("appointments/", include('appointments.urls')),
    path("billings/", include('billing.urls')),
    path("departments/", include('department.urls')),
    path("doctors/", include('doctors.urls')),
    path("medications/", include('medication.urls')),
    path("notifications/", include('notification.urls')),
    path("prescriptions/", include('prescription.urls')),
    path("staff/", include('staff.urls')),
    path("users/", include('users.urls')),
]





# Only enable Silk in DEBUG mode
if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]