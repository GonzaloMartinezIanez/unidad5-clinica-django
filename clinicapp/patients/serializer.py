from rest_framework import serializers
from .models import Patient
from django.utils import timezone
import re

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'last_name', 'dni', 'phone_number', 'birth_date']

    def validate_birth_date(self, value):
        now = timezone.now().date()
        
        if value >= now:
            raise serializers.ValidationError("La fecha de nacimiento no puede ser del futuro")
        
        return value
    
    def validate_dni(self, value):
        # Primero 8 numeros, despues letra mayuscula
        if not re.match("^\d{8}[A-Z]$", value):
            raise serializers.ValidationError("DNI no válido")
        
        return value