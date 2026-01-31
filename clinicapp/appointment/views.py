from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Appointment
from .serializer import AppointmentSerializer

# ViewSet para leer y añadir citas
# Los medicos solo pueden hacer uso del GET
# y los recepcionistas de ambos
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    http_method_names = ['get', 'post']

# Generico para borrar una cita, solo lo pueden hacer los recepcionistas
# Podria estar en el ViewSet anterior, pero de esta forma se usan
# genericos y tiene un ruta propia para hacer el delete
class AppointmentDestroyAPIView(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# Generico para filtrar todas las citas pendientes
class AppointmentListPendingAPIView(generics.ListAPIView):
    queryset = Appointment.objects.filter(status="PEN")
    serializer_class = AppointmentSerializer

# APIView que pueden usar los medicos para añadir un diagnostico a una cita
# y cambiar el estado de pendiente a finalizada
class AppointmentEndAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, id):
        # Gestionar los permisos de manera manual
        if not request.user.groups.filter(name__in=['Medicos']).exists():
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        
        # Cita actual
        appointment = Appointment.objects.get(id = id)

        if not appointment:
            return Response({'error': f'No hay una consulta con este id'}, status=status.HTTP_404_NOT_FOUND)
        
        # Diagnostico pasado por json
        diagnosis = request.data.get('diagnosis', '')
        appointment.diagnosis = diagnosis
        appointment.status = 'FIN'
        appointment.save()
        return Response(AppointmentSerializer(appointment).data, status = status.HTTP_200_OK)