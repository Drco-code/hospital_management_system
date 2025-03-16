from django.urls import path
from department import views

urlpatterns = [
    path(
        "",
        views.DepartmentListCreateAPIView.as_view(),
        name="departments"
    ),
    path(
        "<uuid:department_id>/",
        views.DepartmentRetriveUpdateDestroyAPIView.as_view(),
        name="department"
    ),
    
    
]