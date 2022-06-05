from django.urls import path
from . import views


app_name = "clients"

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='clients'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client-detail'),
    path('client/create/', views.ClientCreate.as_view(), name='client-create'),
    path('client/<int:pk>/update/', views.ClientUpdate.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='client-delete'),
]