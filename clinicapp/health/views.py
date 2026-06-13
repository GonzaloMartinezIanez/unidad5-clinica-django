from rest_framework.views import APIView, status
from rest_framework.response import Response

class HealthApiView(APIView):
    permission_classes = []
    def get(self, request):
        return Response({
            'message': 'La aplicación está en funcionamiento'
        }, status=status.HTTP_200_OK)
