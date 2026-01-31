from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Patient
from appointment.models import Appointment
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token

class PatientTestCase(APITestCase):
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

    def test_list_patients(self):
        url = reverse('patient-viewset-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)
        
    def test_create_patients(self):
        url = reverse('patient-viewset-list')
        data = {
            "name": "José",
            "last_name": "López Fernández",
            "dni": "87654321B",
            "phone_number": "+34 987654321",
            "birth_date": "1998-11-04"
        }
        response = self.client.post(url, data=data, format = "json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['dni'], "87654321B")

    def test_patch_patients(self):
        url = reverse('patient-viewset-detail', args=['12345678A'])
        data = {
            "phone_number": "+34 111222333"
        }
        response = self.client.patch(url, data, format = "json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['phone_number'], "+34 111222333")

    def test_delete_patients(self):
        url = reverse('patient-viewset-detail', args=['12345678A'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_patient_history(self):
        url = reverse('patient-history', args=['12345678A'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)