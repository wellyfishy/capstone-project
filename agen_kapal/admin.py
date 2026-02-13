from django.contrib import admin # type: ignore
from .models import *

admin.site.register(Karyawan)
admin.site.register(Absen)
admin.site.register(Histori)
