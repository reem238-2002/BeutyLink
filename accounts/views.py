from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .decorators import admin_required, salon_required, client_required

# تسجيل دخول
# تسجيل دخول
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # إعادة التوجيه دائمًا للصفحة الرئيسية
            return redirect('home')
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة")
    return render(request, "accounts/login.html")

# تسجيل مستخدم جديد
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "كلمة المرور غير متطابقة!")
            return render(request, "accounts/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل!")
            return render(request, "accounts/signup.html")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.")
        return redirect("login")

    return render(request, "accounts/signup.html")

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