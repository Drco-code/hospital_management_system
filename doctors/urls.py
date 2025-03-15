from django.urls import path
from doctors import views

urlpatterns = [
    path(
        "",
        views.DoctorsListCreateView.as_view(),
        name="doctors"
    ),
    path(
        "<str:doctor_id>/",
        views.DoctorRetrieveUpdateDestroyAPIView.as_view(),
        name="doctor"
    ),
    path(
        "<str:doctor_id>/appointment/<str:appointment_id>/",
        views.DoctorAppointmentRetrieveUpdateDestroyAPIView.as_view(),
        name="doctor-appointment"
    ),
    
    
    
    
]