from django.shortcuts import render
from .forms import SalonRequestForm

def salon_register(request):
    if request.method == 'POST':
        form = SalonRequestForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'salons/success.html')
    else:
        form = SalonRequestForm()

    return render(request, 'salons/register.html', {'form': form})