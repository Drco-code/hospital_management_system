from django.urls import path
from medication import views

urlpatterns = [
    path(
        "",
        views.MedicationListCreateAPIView.as_view(),
        name="medications"
    ),
    path(
        "<uuid:medication_id>/",
        views.MedicationRetrieveUpdateDestroyAPIView.as_view(),
        name="medication"
    ),
    
    
]