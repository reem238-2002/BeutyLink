from django.shortcuts import render
from django.db.models import Q
from accounts.models import Salon, Service

# الصفحة الرئيسية
def home(request):
    return render(request, 'main/index.html')

# صفحات عامة
def salons(request):
    salons_qs = Salon.objects.filter(is_active=True).prefetch_related('services')
    
    # 1. البحث النصي
    search_query = request.GET.get('search', '')
    if search_query:
        salons_qs = salons_qs.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    
    # 2. الفلترة بالمنطقة
    area_filter = request.GET.get('area', '')
    if area_filter:
        salons_qs = salons_qs.filter(area=area_filter)
        
    # 3. الفلترة بالخدمات
    service_filter = request.GET.get('service', '')
    if service_filter:
        salons_qs = salons_qs.filter(services__id=service_filter)
        
    # 4. الفلترة بالفئة السعرية
    price_filter = request.GET.get('price', '')
    if price_filter:
        salons_qs = salons_qs.filter(price_range=price_filter)

    # جلب البيانات اللازمة للفلاتر
    all_areas = Salon.objects.filter(is_active=True).values_list('area', flat=True).distinct()
    all_areas = [a for a in all_areas if a] # تنظيف القيم الفارغة
    all_services = Service.objects.all()

    return render(request, 'main/salons.html', {
        'salons': salons_qs.distinct(),
        'search_query': search_query,
        'all_areas': all_areas,
        'all_services': all_services,
        'current_area': area_filter,
        'current_service': service_filter,
        'current_price': price_filter,
    })

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

# صفحات الحجز (باستخدام app bookings)
def booking(request):
    return render(request, 'bookings/booking.html')

# صفحة لوحة الكوافير
def owner_dashboard(request):
    return render(request, 'main/owner-dashboard.html')  # ← أنشئي هذا الملف

# صفحات الادمن
def admin_login(request):
    return render(request, 'main/admin-login.html')

def admin_dashboard(request):
    return render(request, 'main/admin-dashboard.html')

def admin_bookings(request):
    return render(request, 'main/admin-bookings.html')

def admin_customers(request):
    return render(request, 'main/admin-customers.html')

def admin_reports(request):
    return render(request, 'main/admin-reports.html')

def admin_salons(request):
    return render(request, 'main/admin-salons.html')

def admin_settings(request):
    return render(request, 'main/admin-settings.html')