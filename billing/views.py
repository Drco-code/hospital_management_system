from django.shortcuts import render


from rest_framework import generics, filters, permissions

from billing.models import Billing
from billing.serializers import BillingsSerializer
from billing.filters import BillingFilter

from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class IsAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.billing == request.user


class BillingsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingsSerializer
    filter_backends = [
        filters.OrderingFilter
    ]

    filterset_class = BillingFilter
    search_fields = ['total_amount', 'payment_date']

    #setup authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class BillingRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingsSerializer
    lookup_field = 'billing_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):

        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsAdminOrOwner]
        return super().get_permissions()



