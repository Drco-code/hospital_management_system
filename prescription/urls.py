from django.urls import path
from prescription import views

urlpatterns = [
    path(
        "",
        views.PrescriptionListCreateAPIView.as_view(),
        name="prescriptions"
    ),
    path(
        "<str:prescription_id>/",
        views.PrescriptionRetrieveUpdateDestroyAPIView.as_view(),
        name="prescription"
    ),
    path(
        "<str:prescription_id>/medication/<str:medication_id>/",
        views.PrescriptionMedicationRetrieveUpdateDestroyAPIView.as_view(),
        name="prescription-medication"
    ),
        
    
]