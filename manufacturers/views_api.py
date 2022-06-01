from rest_framework import viewsets, permissions

from .serializers import ManufacturerSerializer
from .models import Manufacturer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]