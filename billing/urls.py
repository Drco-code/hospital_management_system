from django.urls import path
from billing import views

urlpatterns = [
    path(
        "",
        views.BillingsListCreateAPIView.as_view(),
        name="billings"
    )
    
    
]