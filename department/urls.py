from django.urls import path
from department import views

urlpatterns = [
    path(
        "",
        views.DepartmentListCreateAPIView.as_view(),
        name="departments"
    )
    
    
]