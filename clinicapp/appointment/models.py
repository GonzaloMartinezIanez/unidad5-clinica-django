from django.db import models
from patients.models import Patient

# Modelo de las citas
class Appointment(models.Model):
    # Almacenar el estado de una cita
    STATUS_CHOICE = {
        "PEN": "Pendiente",
        "FIN": "Finalizada",
    }
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    diagnosis = models.TextField(blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICE, default='PEN')

    def __str__(self):
        return f"{self.patient}: {self.appointment_date}"