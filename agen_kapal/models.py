from django.db import models # type: ignore
from django.contrib.auth.models import User


# Untuk Web-profil
class Tentang(models.Model):
    tentang = models.TextField()
    last_edited = models.DateTimeField(null=True, blank=True)

class Karyawan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    nama_karyawan = models.CharField(max_length=100, null=True, blank=True)
    detail_karyawan = models.CharField(max_length=100, null=True, blank=True) # Sebagai CEO, Manager, dll 
    no_hp = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nama_karyawan or self.user.username
    
class Absen(models.Model):
    STATUS = [
        ('1', 'Hadir'),
        ('2', 'Izin'),
        ('3', 'Sakit'),
        ('4', 'Alpha')
    ]
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    file_foto = models.FileField(upload_to='berkas_absen/', null=True, blank=True) # Digunakan untuk Face Recognition/Bukti foto kerja
    keterangan = models.TextField()
    status = models.CharField(choices=STATUS, default='1')
    tanggal = models.DateTimeField(auto_now_add=True)

class Layanan(models.Model):
    STATUS = [
        ('1', 'Buka'),
        ('2', 'Penuh'),
        ('3', 'Tutup')
    ]
    nama_layanan = models.CharField(max_length=100, null=True, blank=True)
    detail_layanan = models.TextField()
    status = models.CharField(choices=STATUS, default='1')
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    diedit_pada = models.DateTimeField(auto_now=True)

# Untuk panel admin
class Kapal(models.Model):
    imo = models.CharField(max_length=50, null=True, blank=True)

class Client(models.Model):
    nama_client = models.CharField(max_length=100, null=True, blank=True)
    kapal = models.ForeignKey(Kapal, on_delete=models.SET_NULL, null=True, blank=True)
    no_hp = models.CharField(max_length=20)
    file = models.FileField(upload_to='berkas_client/', null=True, blank=True)

class Request(models.Model):
    STATUS = [
        ('0', 'Menunggu'),
        ('1', 'Diproses'),
        ('2', 'Selesai'),
        ('3', 'Dibatalkan')
    ]

    detail = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=STATUS, default='0')

class ToDoList(models.Model):
    STATUS = [
        ('0', 'Belum'),
        ('2', 'Selesai'),
        ('3', 'Dibatalkan')
    ]

    request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True, blank=True) # Opsional
    detail = models.TextField()
    diedit_oleh = models.ForeignKey(Karyawan, on_delete=models.SET_NULL, null=True, blank=True)
    diedit_pada = models.DateTimeField(auto_now=True)

class FileKategori(models.Model):
    nama_kategori = models.CharField(max_length=50, null=True, blank=True) # Untuk keperluan TF-IDF

class File(models.Model):
    kapal = models.ForeignKey(Kapal, on_delete=models.CASCADE, null=True, blank=True)
    request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='berkas_kapal/', null=True, blank=True)
    kategori = models.ForeignKey(FileKategori, on_delete=models.SET_NULL, null=True, blank=True)