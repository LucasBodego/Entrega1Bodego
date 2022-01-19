from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio),
    path('clientes/', views.clientes),
    path('repuestos/', views.repuestos),
    path('presupuestos/', views.presupuestos),
    path('entregas/', views.entregas),
]
    