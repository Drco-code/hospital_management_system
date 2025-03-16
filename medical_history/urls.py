from django.urls import path
from medical_history import views

urlpatterns = [
    path(
        "",
        views.MedicalHistoryListCreateAPIView.as_view(),
        name="Medical-Histories"
    ),
    path(
        "<uuid:history_id>/",
        views.MedicalHistoryRetrieveUpdateDestroyAPIView.as_view(),
        name="Medical-History"
    )
    
    
]
