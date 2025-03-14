from django.urls import path
from doctors import views

urlpatterns = [
    path(
        "",
        views.DoctorsListCreateView.as_view(),
        name="doctors"
    )
    
    
]