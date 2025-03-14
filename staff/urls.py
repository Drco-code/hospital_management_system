from django.urls import path
from staff import views

urlpatterns = [
    path(
        "",
        views.StaffListCreateAPIView.as_view(),
        name="staff"
    )
    
    
]