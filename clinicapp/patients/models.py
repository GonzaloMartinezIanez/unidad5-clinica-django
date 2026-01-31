from django.db import models

# Modelo del paciente
class Patient(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    dni = models.CharField(unique=True, max_length=9, null=False, blank=False)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"