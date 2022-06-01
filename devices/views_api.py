from rest_framework import viewsets, permissions

from .serializers import DeviceSerializer
from .models import Device


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


