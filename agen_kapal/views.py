from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        'on': 'index',
    }
    return render(request, 'landing/index.html', context)

def layanan(request):
    all_layanan = Layanan.objects.all()

    context = {
        'on': 'layanan',
        'all_layanan': all_layanan,
    }
    return render(request, 'landing/layanan.html', context)

def dashboard(request):
    context = {
        'on': 'utama',
    }
    return render(request, 'admin/dashboard.html', context)