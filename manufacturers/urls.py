from django.urls import path
from . import views

app_name = "manufacturers"

urlpatterns = [
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturers'),
    path('manufacturer/<int:pk>', views.ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    path('manufacturer/create/', views.ManufacturerCreate.as_view(), name='manufacturer-create'),
    path('manufacturer/<int:pk>/update/', views.ManufacturerUpdate.as_view(), name='manufacturer-update'),
    path('manufacturer/<int:pk>/delete/', views.ManufacturerDelete.as_view(), name='manufacturer-delete'),
]