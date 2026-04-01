from django.shortcuts import render, redirect
from .models import SalonRequest

def salon_register(request):
    if request.method == 'POST':
        SalonRequest.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            location=request.POST.get('location'),
            shop_image=request.FILES.get('shop_image'),
            logo=request.FILES.get('logo'),
        )
        return render(request, 'salons/success.html')  # صفحة نجاح

    return render(request, 'salons/register.html')