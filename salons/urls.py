from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.salon_register, name='salon_register'),
    path('blacklist/', views.blacklist_page, name='blacklist'),
    path('blacklist/add/<int:salon_id>/', views.blacklist_salon, name='blacklist_salon'),
    path('blacklist/remove/<int:salon_id>/', views.remove_from_blacklist, name='remove_from_blacklist'),
]