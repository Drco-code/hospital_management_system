from django.urls import path
from appointments import views

urlpatterns = [
    path(
        "",
        views.AppointmentListCreateAPIView.as_view(),
        name="appointments"
    ),
    path(
        "upcoming/",
        views.UpcomingAppointmentListAPIAPIView.as_view(),
        name="upcoming-appointment"
    ),
    path(
        "past/",
        views.PastAppointmentListAPIAPIView.as_view(),
        name="past-appointment"
    ),
    path(
        "<str:appointment_id>/",
        views.AppointmentRetrieveUpdateDestroyAPIView.as_view(),
        name="appointment"
    ),
    
    
]