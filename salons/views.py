from django.shortcuts import render
from .forms import SalonRequestForm
from .models import SalonRequest
from django.utils import timezone
from django.http import JsonResponse

def salon_register(request):
    if request.method == 'POST':
        form = SalonRequestForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'salons/success.html')
    else:
        form = SalonRequestForm()

    return render(request, 'salons/register.html', {'form': form})

def blacklist_page(request):
    salons = SalonRequest.objects.filter(is_blacklisted=True)
    return render(request, "blacklist.html", {"salons": salons})

def blacklist_salon(request, salon_id):
    salon = SalonRequest.objects.get(id=salon_id)
    salon.is_blacklisted = True
    salon.blacklist_reason = request.POST.get("reason", "")
    salon.blacklisted_at = timezone.now()
    salon.save()

    return JsonResponse({"message": "تمت الإضافة للقائمة السوداء"})

def remove_from_blacklist(request, salon_id):
    salon = SalonRequest.objects.get(id=salon_id)
    salon.is_blacklisted = False
    salon.blacklist_reason = None
    salon.blacklisted_at = None
    salon.save()

    return JsonResponse({"message": "تمت الإزالة من القائمة السوداء"})
