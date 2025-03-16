from django.urls import path
from patients import views

urlpatterns = [
        path(
        "",
        views.PatientListCreateAPIView.as_view(),
        name="patients"
    ),
    path(
        "<str:patient_id>/",
        views.PatientRetriveUpdateDeleteAPIView.as_view(),
        name="patient"
    ),
    path(
        "<str:patient_id>/medical-history/<str:history_id>/",
        views.PatientMedicalRecordsRetrieveUpdateDestroyView.as_view(),
        name="patient-medical-history"
    ),
    path(
        "<str:patient_id>/appointment/<str:appointment_id>/",
        views.PatientAppointmentRetrieveUpdateDestroyView.as_view(),
        name="patient-appointment"
    ),
    
]
