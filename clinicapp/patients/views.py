from django.shortcuts import render
from .models import Patient
from .serializer import PatientSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from .serializer import PatientSerializer
from rest_framework.permissions import IsAuthenticated
from appointment.models import Appointment
from appointment.serializer import AppointmentSerializer



# Viewset para CRUD de pacientes
# Los recepcionistas tienen permiso para todo el CRUD
# Los medicos solo pueden leer
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'dni'

# APIView que enlaza dos modelos y devuelve el historial medico de un
# paciente mediante su DNI
class PatientHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, dni):
        # Como esta view no hace uso de queryset, djangoModelPermissions no tiene
        # acceso y hay que gestionar los permisos manualmente. En este caso
        # tanto medicos como recepcionistas pueden listar el historial de un paciente
        if not request.user.groups.filter(name__in=['Medicos', 'Recepcionistas']).exists():
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        
        # Todas las citas del paciente
        appointment = Appointment.objects.filter(patient__dni = dni)
        if not appointment:
            return Response({'error': f'Esta persona no tiene ninguna consulta'}, status=status.HTTP_404_NOT_FOUND)

        serializer_serializer = AppointmentSerializer(appointment, many=True)

        # Datos del paciente
        patient = Patient.objects.get(dni = dni)
        patient_serializer = PatientSerializer(patient)
        return Response({'patient': patient_serializer.data,'appointments': serializer_serializer.data}, status = status.HTTP_200_OK)
   