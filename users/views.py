from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from users.filters import UserFilter
from rest_framework import filters
from rest_framework.permissions import BasePermission, SAFE_METHODS



# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.order_by('id')
    serializer_class = UserSerializer
    filter_backends = [
        # DjangoFilterBackend,  # sets the filter for this view
       filters.OrderingFilter,
       filters.SearchFilter,
                       ]
    # filterset_fields = ['username', 'id', 'first_name', 'last_name', 'date_joined', 'user_role'] # for equality based filtering
    
    # Enable filtering
    filterset_class = UserFilter 

    # Enable searching and ordering
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['id', 'date_joined', 'username']


    def get_permissions(self):

        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
# Custom permission to allow only the user or an admin to edit/delete
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # Read-only access for all authenticated users
        return request.user.is_staff or obj == request.user  # Only owner or admin can edit/delete

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "id" # Ensures lookup by 'id' in the URL
    authentication_classes = [JWTAuthentication, SessionAuthentication] # applies JWT ath on the view

    def get_permissions(self):

        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()

