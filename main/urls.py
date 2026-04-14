from django.urls import path, include
from . import views

urlpatterns = [
    # الصفحة الرئيسية
    path('', views.home, name='home'),

    # صفحات عامة
    path('salons/', views.salons, name='salons'),  # ← تم إضافة صفحة الكوافيرات
    path('contact/', views.contact, name='contact'),

    # رابط الحجز مع app bookings
    path('booking/', include('bookings.urls')),

    # صفحات الادمن
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-bookings/', views.admin_bookings, name='admin_bookings'),
    path('admin-customers/', views.admin_customers, name='admin_customers'),
    path('admin-reports/', views.admin_reports, name='admin_reports'),
    path('admin-salons/', views.admin_salons, name='admin_salons'),
    path('admin-settings/', views.admin_settings, name='admin_settings'),

    # صفحة لوحة الكوافير
    path('owner-dashboard/', views.owner_dashboard, name='owner_dashboard'),
]