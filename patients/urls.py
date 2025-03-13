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
    )
    
]
