from django.urls import path
from users import views

urlpatterns = [
    path(
        "",
        views.UserListCreateAPIView.as_view(),
        name="user-list"
    ),
    path(
        "<int:id>/",
        views.UserRetrieveUpdateDestroyAPIView.as_view(),
        name="user-detail"
    ),
    
    
]