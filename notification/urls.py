from django.urls import path
from notification import views

urlpatterns = [
    path(
        "",
        views.NotificationListCreateAPIView.as_view(),
        name="notifications"
    ),
    path(
        "<uuid:notification_id>/",
        views.NotificationRetieveUpdateDestroyAPIView.as_view(),
        name="notification"
    ),
    
    
]