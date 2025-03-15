from django.urls import path
from billing import views

urlpatterns = [
    path(
        "",
        views.BillingsListCreateAPIView.as_view(),
        name="billings"
    ),
    path(
        "<str:billing_id>/",
        views.BillingsRetieveUpdateAPIView.as_view(),
        name="billing"
    ),
    path(
        "<str:billing_id>/<str:patient_id>/billing-history/",
        views.PatientBillingListAPIView.as_view(),
        name="billing"
    ),
    
    
]