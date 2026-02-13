from django.shortcuts import render, redirect  # type: ignore
from .models import *
from django.http import JsonResponse # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib import messages # type: ignore

def ajax_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Username atau password salah."})
    return JsonResponse({"success": False, "error": "Invalid request"})

def logoutfunc(request):
    logout(request)
    return redirect('index')

# Admin Panel
def dashboard(request):
    all_histori = Histori.objects.all().order_by('-pk')
    context = {
        'on': 'utama',
        'all_histori': all_histori,
    }
    return render(request, 'admin/dashboard.html', context)

def karyawan(request):
    all_karyawan = Karyawan.objects.all()
    all_karyawan_off_count = all_karyawan.filter(status='2').count()

    if request.method == 'POST':
        if request.POST.get('tipe_submit') == 'tambah_karyawan':
            username = request.POST.get('username')
            password = request.POST.get('password')
            nama_lengkap = request.POST.get('nama_lengkap')
            jabatan = request.POST.get('jabatan')
            no_hp = request.POST.get('no_hp')
            status = '1' if request.POST.get('status') == 'on' else '2'

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username sudah digunakan. Silakan pilih username lain.")
                return redirect('karyawan')

            user = User.objects.create_user(username=username, password=password, first_name=nama_lengkap)
            karyawan = Karyawan.objects.create(user=user, nama_karyawan=nama_lengkap, detail_karyawan=jabatan, no_hp=no_hp, status=status)
            Histori.objects.create(tipe_histori='Karyawan', detail_histori=f'{request.user.username} melakukan penambahan karyawan {karyawan.nama_karyawan}')
            messages.success(request, "Karyawan berhasil ditambahkan!")
        
        if request.POST.get('tipe_submit') == 'edit_karyawan':
            karyawan_pk = request.POST.get('karyawan_pk')
            karyawan = Karyawan.objects.get(pk=karyawan_pk)

            username = request.POST.get('username')
            password = request.POST.get('password')
            nama_lengkap = request.POST.get('nama_lengkap')
            jabatan = request.POST.get('jabatan')
            no_hp = request.POST.get('no_hp')
            status = request.POST.get('status')

            karyawan.nama_karyawan = nama_lengkap
            karyawan.detail_karyawan = jabatan
            karyawan.no_hp = no_hp
            karyawan.status = status
            karyawan.save()

            Histori.objects.create(tipe_histori='Karyawan', detail_histori=f'{request.user.username} melakukan pengeditan karyawan {karyawan.nama_karyawan}')

            messages.success(request, "Karyawan berhasil diperbarui!")

        return redirect('karyawan')
    context = {
        'on': 'karyawan',
        'all_karyawan': all_karyawan,
        'all_karyawan_off_count': all_karyawan_off_count,
    }
    return render(request, 'admin/karyawan.html', context)

# Web Profil
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
