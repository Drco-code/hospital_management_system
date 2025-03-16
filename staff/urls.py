from django.urls import path
from staff import views

urlpatterns = [
    path(
        "",
        views.StaffListCreateAPIView.as_view(),
        name="all-staff"
    ),
    path(
        "<uuid:staff_id>/",
        views.StaffRetriveUpdateDestroyAPIView.as_view(),
        name="staff"
    ),
    
    
]