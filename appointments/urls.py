from django.urls import path
from appointments import views

urlpatterns = [
    path(
        "",
        views.AppointmentListCreateAPIView.as_view(),
        name="appointments"
    )
    
    
]