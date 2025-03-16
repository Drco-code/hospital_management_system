from django.urls import path
from prescription import views

urlpatterns = [
    path(
        "",
        views.PrescriptionListCreateAPIView.as_view(),
        name="prescriptions"
    ),
    path(
        "<uuid:prescription_id>/",
        views.PrescriptionRetrieveUpdateDestroyAPIView.as_view(),
        name="prescription"
    ),
    path(
        "<uuid:prescription_id>/medication/<uuid:medication_id>/",
        views.PrescriptionMedicationRetrieveUpdateDestroyAPIView.as_view(),
        name="prescription-medication"
    ),
    
    
]