from django.urls import path
from .views import salon_register

urlpatterns = [
    path('register/', salon_register, name='salon_register'),
]