from django.urls import path
from . import views

app_name = "devices"

urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name='devices'),
    path('device/<int:pk>', views.DeviceDetailView.as_view(), name='device-detail'),
    path('device/create/', views.DeviceCreate.as_view(), name='device-create'),
    path('device/<int:pk>/update/', views.DeviceUpdate.as_view(), name='device-update'),
    path('device/<int:pk>/delete/', views.DeviceDelete.as_view(), name='device-delete'),
]