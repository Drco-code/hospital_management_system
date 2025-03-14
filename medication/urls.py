from django.urls import path
from medication import views

urlpatterns = [
    path(
        "",
        views.MedicationListCreateAPIView.as_view(),
        name="medications"
    )
    
    
]