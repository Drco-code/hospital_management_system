
from patients.serializers import PatientSerializer

from patients.models import Patient

from medical_history.models import MedicalHistory


from rest_framework import generics

# Create your views here.


class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    


class PatientRetriveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_url_kwarg = 'patient_id'

# class PatientMedicalRecordsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MedicalHistory
    
