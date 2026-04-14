from django.db import models
from django.core.exceptions import ValidationError


# 🔥 تحقق رقم الهاتف اليمني
def validate_yemen_phone(value):
    if len(value) != 9:
        raise ValidationError("رقم الهاتف يجب أن يكون 9 أرقام")

    if not value.startswith(('77', '78', '73', '70', '71')):
        raise ValidationError("رقم الهاتف يجب أن يبدأ بـ 77 أو 78 أو 73 أو 70 أو 71")


class SalonRequest(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=9, validators=[validate_yemen_phone])
    email = models.EmailField()
    location = models.CharField(max_length=255)

    password = models.CharField(max_length=128)  # كلمة المرور التي يدخلها الكوافير عند الطلب
    shop_image = models.ImageField(upload_to='salon_requests/')
    commercial_registration = models.ImageField(upload_to='salon_requests/')
    logo = models.ImageField(upload_to='salon_logos/')

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name