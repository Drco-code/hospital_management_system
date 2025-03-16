from django.urls import path
from billing import views

urlpatterns = [
    path(
        "",
        views.BillingsListCreateAPIView.as_view(),
        name="billings"
    ),
    path(
        "<uuid:billing_id>/",
        views.BillingRetriveUpdateDestroyAPIView.as_view(),
        name="billing"
    ),
    
    
]