from django.urls import reverse
from rest_framework.test import APITestCase
from patients.models import Patient
from .models import Appointment
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token

class AppointmentReceptionistTestCase(APITestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            name = "Pablo",
            last_name = "Martínez López",
            dni = "12345678A",
            phone_number = "+34 123456789",
            birth_date = "1985-05-23"
        )

        self.cita1 = Appointment.objects.create(
            patient = self.patient,
            appointment_date = "2026-05-02 13:45:00"
        )

        self.cita2 = Appointment.objects.create(
            patient = self.patient,
            appointment_date = "2026-05-05 15:15:00"
        )

        self.user = User.objects.create_superuser(username="example", password="1234")
        group, created = Group.objects.get_or_create(name='Recepcionistas')
        self.user.groups.add(group)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_appointment(self):
        url = reverse('appointment-viewset-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_create_appointment(self):
        url = reverse('appointment-viewset-list')
        data = {
            "patient" : "1",
            "appointment_date": "2026-03-15 17:30:00"
        }
        response = self.client.post(url, data=data, format = "json")
        self.assertEqual(response.status_code, 201)

    def test_delete_patients(self):
        url = reverse('appointment-destroy', args=['1'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_list_pending(self):
        url = reverse('appointment-pending')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AppointmentTestCase(APITestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            name = "Pablo",
            last_name = "Martínez López",
            dni = "12345678A",
            phone_number = "+34 123456789",
            birth_date = "1985-05-23"
        )

        self.cita1 = Appointment.objects.create(
            patient = self.patient,
            appointment_date = "2026-05-02 13:45:00"
        )

        self.cita2 = Appointment.objects.create(
            patient = self.patient,
            appointment_date = "2026-05-05 15:15:00"
        )

        self.user = User.objects.create_superuser(username="example", password="1234")
        group, created = Group.objects.get_or_create(name='Medicos')
        self.user.groups.add(group)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_end_appointmnet(self):
        url = reverse('appointment-end', args=['1'])
        data = {
            "diagnosis": "Diagnostico de ejemplo."
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "FIN")