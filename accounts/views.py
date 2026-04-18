from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Salon
from .decorators import admin_required, salon_required, client_required

# تسجيل دخول
# تسجيل دخول
def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            context['username'] = username
            context['errors'] = {
                'username': "اسم المستخدم أو كلمة المرور غير صحيحة"
            }
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة")
    return render(request, "accounts/login.html", context)

# تسجيل مستخدم جديد
def signup_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        context['username'] = username
        context['email'] = email

        if password != password2:
            context['errors'] = {
                'password2': "كلمة المرور غير متطابقة!"
            }
            messages.error(request, "كلمة المرور غير متطابقة!")
            return render(request, "accounts/signup.html", context)

        if User.objects.filter(username=username).exists():
            context['errors'] = {
                'username': "اسم المستخدم موجود بالفعل!"
            }
            messages.error(request, "اسم المستخدم موجود بالفعل!")
            return render(request, "accounts/signup.html", context)

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.")
        return redirect("login")

    return render(request, "accounts/signup.html", context)

def logout_view(request):
    logout(request)
    return redirect('home')



# Dashboards
@admin_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@salon_required
def salon_dashboard(request):
    return render(request, 'accounts/salon_dashboard.html')

@client_required
def client_dashboard(request):
    return render(request, 'accounts/client_dashboard.html')

def browse_salons(request):
    salons = Salon.objects.filter(is_active=True)

    search = request.GET.get('search')
    if search:
        salons = salons.filter(name__icontains=search)

    return render(request, 'browse_salons.html', {
        'salons': salons
    })