from django.urls import path
from users import views

urlpatterns = [
    path(
        "",
        views.UserListCreataAPIView.as_view(),
        name="users"
    )
    
    
]