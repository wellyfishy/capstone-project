from django.db import models # type: ignore


# Untuk Web-profil
class Tentang(models.Model):
    tentang = models.TextField()
    last_edited = models.DateTimeField(null=True, blank=True)

class Karyawan(models.Model):
    nama_karyawan = models.CharField(max_length=100, null=True, blank=True)

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

class FileKategori(models.Model):
    nama_kategori = models.CharField(max_length=50, null=True, blank=True)

class File(models.Model):
    kapal = models.ForeignKey(Kapal, on_delete=models.CASCADE, null=True, blank=True)
    request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='berkas_kapal/', null=True, blank=True)
    kategori = models.ForeignKey(FileKategori, on_delete=models.SET_NULL, null=True, blank=True)