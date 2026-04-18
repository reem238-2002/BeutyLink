from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'أدمن'),
        ('salon', 'كوافير'),
        ('client', 'عميل'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# إنشاء Profile تلقائياً عند إضافة مستخدم جديد
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# حفظ Profile بعد تحديث الـ User، مع التأكد من وجوده
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Lucide icon name")

    def __str__(self):
        return self.name

class Salon(models.Model):
    PRICE_CHOICES = (
        (1, '$'),
        (2, '$$'),
        (3, '$$$'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='salons/', help_text="Background image")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Small logo/avatar")
    rating = models.FloatField(default=0)
    location = models.CharField(max_length=255, default='صنعاء')
    area = models.CharField(max_length=100, blank=True, null=True, help_text="Neighborhood/Area")
    price_range = models.IntegerField(choices=PRICE_CHOICES, default=2)
    services = models.ManyToManyField(Service, related_name='salons')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.salon.name}"