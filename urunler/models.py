from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    def __str__ (self):
        return self.isim

class AltKategori(models.Model):
    isim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim

class Urunler(models.Model):
    satici = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
    altkategori = models.ManyToManyField(AltKategori, blank=True)
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(max_length=1000)
    fiyat = models.IntegerField()
    resim = models.FileField(upload_to='urunler/', null=True)

    def __str__(self):
        return self.isim
    

class Sepet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    urun = models.ForeignKey(Urunler, on_delete=models.CASCADE)
    adet = models.IntegerField()
    toplamFiyat = models.IntegerField()
    odendiMi = models.BooleanField(default=False)
    def __str__(self):
        return self.owner.username