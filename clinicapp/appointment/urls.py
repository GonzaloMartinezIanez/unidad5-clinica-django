from django.urls import path, include
from .views import AppointmentViewSet, AppointmentListPendingAPIView, AppointmentDestroyAPIView, AppointmentEndAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewset', AppointmentViewSet, basename='appointment-viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('pending/', AppointmentListPendingAPIView.as_view(), name='appointment-pending'),
    path('destroy/<int:pk>/', AppointmentDestroyAPIView.as_view(), name='appointment-destroy'),
    path('end/<int:id>/', AppointmentEndAPIView.as_view(), name='appointment-end'),
]