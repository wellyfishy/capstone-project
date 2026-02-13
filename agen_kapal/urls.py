from django.urls import path # type: ignore
from .views import *

urlpatterns = [
    # Auth
    path("ajax-login/", ajax_login, name="login"),
    path('logout', logoutfunc, name='logout'),

    # Web profile
    path('', index, name='index'),
    path('layanan/', layanan, name='layanan'),

    # Admin
    path('admin_panel/dashboard', dashboard, name='dashboard'),
    path('admin_panel/karyawan', karyawan, name='karyawan'),
]
