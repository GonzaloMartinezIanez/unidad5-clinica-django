from .views import HealthApiView
from django.urls import path

urlpatterns = [
    path('', HealthApiView.as_view(), name='health')
]