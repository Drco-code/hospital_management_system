from django.urls import path
from notification import views

urlpatterns = [
    path(
        "",
        views.NotificationListCreateAPIView.as_view(),
        name="notifications"
    )
    
    
]