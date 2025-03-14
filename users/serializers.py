from rest_framework import serializers

from users.models import User
# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','user_role', 'email', 'first_name', 'last_name',
        'is_staff', 'is_active', 'date_joined')
