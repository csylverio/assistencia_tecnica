"""assistencia_tecnica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from devices.views_api import DeviceViewSet
from manufacturers.views_api import ManufacturerViewSet

router = routers.DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturers')
router.register(r'devices', DeviceViewSet, basename='devices')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^', include('base.urls')),
    re_path(r'^', include('clients.urls')),
    re_path(r'^', include('devices.urls')),
    re_path(r'^', include('manufacturers.urls')),
]
