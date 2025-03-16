from django.shortcuts import render

from rest_framework import generics, filters

from department.models import Department
from department.serializers import DepartmentSerializer

from department.filters import DepartmentFilter

from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser

# Create your views here.


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [
        filters.SearchFilter
    ]

    filterset_class = DepartmentFilter
    search_fields = ['name', 'description']

    authentication_classes = [
        SessionAuthentication, 
        JWTAuthentication
        ]
    
    def get_permissions(self):
        """Allow any user to GET, but require admin permissions to create a department."""
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]
    
class DepartmentRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_url_kwarg = 'department_id'
    authentication_classes = [
        SessionAuthentication, 
        JWTAuthentication
        ]


    def get_permissions(self):
        """Allow any user to GET, but require admin permissions to update or delete a department."""
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]