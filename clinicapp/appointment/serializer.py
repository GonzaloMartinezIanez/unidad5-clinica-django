from django.utils import timezone
from rest_framework import serializers
from .models import Appointment
from patients.models import Patient
from patients.serializer import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    patient_dni = serializers.CharField(source='patient.dni', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'patient_dni', 'appointment_date', 'diagnosis', 'status']

    def validate_appointment_date(self, value):
        now = timezone.now()
        hour = value.hour

        if value <= now:
            raise serializers.ValidationError("La cita no puede ser del pasado")
        
        if hour < 8 or hour >= 20:
            raise serializers.ValidationError("La cita debe ser en horario laboral")
        
        return value