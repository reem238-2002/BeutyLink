# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # هذا ضروري
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('salon-dashboard/', views.salon_dashboard, name='salon_dashboard'),
    path('client-dashboard/', views.client_dashboard, name='client_dashboard'),
]