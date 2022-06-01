# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Manufacturer, Device

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
        
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'