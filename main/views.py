from django.shortcuts import render

# الصفحة الرئيسية
def home(request):
    return render(request, 'main/index.html')

# صفحات عامة
def salons(request):
    return render(request, 'main/salons.html')  # ← أنشئي هذا الملف

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