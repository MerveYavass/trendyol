from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('urunler/', urunler, name='urunler'),
    path('urunOlustur/', create, name='urunOlustur'),
    path('sepet/', sepet, name='sepet'),
    path('urun/<int:urunId>', urundetay, name='detay')
]