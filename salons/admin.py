from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import SalonRequest

@admin.register(SalonRequest)
class SalonRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    search_fields = ('name', 'phone')

    actions = ['approve_salon', 'reject_salon']

    def approve_salon(self, request, queryset):
        for salon_request in queryset:
            if not salon_request.is_approved:
                # إنشاء المستخدم
                user = User.objects.create_user(
                    username=salon_request.phone,
                    email=salon_request.email,
                    password=salon_request.password
                )
                user.profile.role = 'salon'
                user.profile.save()

                # تحديث حالة الطلب
                salon_request.is_approved = True
                salon_request.save()

                # إرسال إيميل HTML
                subject = "تم قبول طلبك ككوافر"
                from_email = 'admin@beautylink.com'
                to = [salon_request.email]

                html_content = render_to_string('emails/salon_approved.html', {
                    'name': salon_request.name,
                    'username': salon_request.phone,
                    'password': salon_request.password,
                    'site_name': 'بيوتي لينك',
                    'site_url': 'http://127.0.0.1:8000/accounts/login/'
                })

                msg = EmailMultiAlternatives(subject, '', from_email, to)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

        self.message_user(request, "تمت الموافقة على الطلبات المحددة ✅")

    approve_salon.short_description = "الموافقة على الطلب"

    def reject_salon(self, request, queryset):
        for salon_request in queryset:
            if not salon_request.is_approved:
                subject = "تم رفض طلبك ككوافر"
                from_email = 'admin@beautylink.com'
                to = [salon_request.email]

                html_content = render_to_string('emails/salon_rejected.html', {
                    'name': salon_request.name,
                    'site_name': 'بيوتي لينك'
                })

                msg = EmailMultiAlternatives(subject, '', from_email, to)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                # حذف الطلب بعد الرفض
                salon_request.delete()

        self.message_user(request, "تم رفض الطلبات المحددة ❌")

    reject_salon.short_description = "رفض الطلب"