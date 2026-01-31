from django.urls import path, include
from .views import PatientViewSet, PatientHistoryAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewset', PatientViewSet, basename='patient-viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('history/<str:dni>/', PatientHistoryAPIView.as_view(), name='patient-history'),
]