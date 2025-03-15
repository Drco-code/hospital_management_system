from django.urls import path
from appointments import views

from datetime import datetime
urlpatterns = [
    path(
        "",
        views.AppointmentListCreateAPIView.as_view(),
        name="appointments"
    ),
    path(
        "upcoming/",
        views.UpcomingAppointmentListView.as_view(),
        name="upcoming-appointment"
    ),
    path(
        "past/",
        views.PastAppointmentListView.as_view(),
        name="upcoming-appointment"
    ),
    path(
        "<str:appointment_id>/",
        views.AppointmentRetrieveUpdateDestroyAPIView.as_view(),
        name="appointment"
    ),
    
    
    
    
]