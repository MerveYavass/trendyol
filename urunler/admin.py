from django.contrib import admin
from .models import *
class SepetAdmin(admin.ModelAdmin):
    list_display = ('owner', 'urun', 'adet', 'toplamFiyat', 'odendiMi')
    list_filter = ('owner', 'odendiMi')
# Register your models here.
admin.site.register(Urunler)
admin.site.register(Kategori)
admin.site.register(AltKategori)
admin.site.register(Sepet, SepetAdmin)
