from django.shortcuts import render

from rest_framework import generics

from department.models import Department
from department.serializers import DepartmentSerializer

# Create your views here.


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
