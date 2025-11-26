from django.urls import path
from .views import *

urlpatterns = [
    # Web profile
    path('', index, name='index'),
    path('layanan/', layanan, name='layanan'),

    # Admin
    path('admin_panel/dashboard', dashboard, name='dashboard'),
]
