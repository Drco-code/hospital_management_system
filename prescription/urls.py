from django.urls import path
from prescription import views

urlpatterns = [
    path(
        "",
        views.PrescriptionListCreateAPIView.as_view(),
        name="prescriptions"
    )
    
    
]