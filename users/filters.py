import django_filters

from users.models import User

class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields = {
            'id': ['exact'], # Filter by exacT User ID
            'username': ['exact', 'icontains'], # Exact match or case-insensitive partial match
            'email': ['exact', 'icontains'], # Exact match or case-insensitive partial match
            'user_role': ['exact'], # Filter by exact user role
            'is_active': ['exact'], # Filter active/inactive users
            'is_staff': ['exact'], # Filter staff users
            'date_joined': ['gte', 'lte'] # Filter by date range
        }


