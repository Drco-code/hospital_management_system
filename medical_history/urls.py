from django.urls import path
from medical_history import views

urlpatterns = [
    path(
        "",
        views.MedicalHistoryListCreateAPIView.as_view(),
        name="Medical-History"
    )
    
    
]
