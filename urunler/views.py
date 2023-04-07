from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def urunler(request):
    urunlerim = Urunler.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunlerim = Urunler.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search) |
            Q(satici__username__icontains = search)
        )
    if request.method == 'POST':
        if request.user.is_authenticated:
            urunId = request.POST['urunId']
            urunum = Urunler.objects.get(id = urunId)
            adet = request.POST['adet']
            if Sepet.objects.filter(owner = request.user, urun = urunum, odendiMi = False).exists():
                sepet = Sepet.objects.get(owner = request.user, urun = urunum, odendiMi = False)
                sepet.adet += int(adet)
                sepet.toplamFiyat = sepet.adet * sepet.urun.fiyat
                sepet.save()
                messages.success(request, 'Sepete eklendi')
                return redirect('index')
            else:
                sepet = Sepet.objects.create(
                    owner = request.user,
                    urun = urunum,
                    adet = adet,
                    toplamFiyat = int(adet) * urunum.fiyat
                )
                sepet.save()
                messages.success(request, 'Sepete Eklendi')
                return redirect('index')
        else:
            messages.warning(request, 'Lütfen giriş yapınız.')
            return redirect('index')
    context = {
        'urunlerim':urunlerim,
        'search':search
    }
    return render(request, 'urun.html', context)

def create(request):
    form = UrunlerForm()
    if request.method == 'POST':
        form = UrunlerForm(request.POST, request.FILES)
        if form.is_valid():
            urun = form.save(commit=False)
            urun.satici = request.user
            urun.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'urunOlustur.html', context)

def sepet(request):
    user = request.user
    sepetim = Sepet.objects.filter(owner = user, odendiMi = False)
    toplam = 0
    for i in sepetim:
        toplam += i.toplamFiyat
    if request.method == 'POST':
        if 'sil' in request.POST:
            urunId = request.POST['urunId']
            silinen = Sepet.objects.get(id = urunId)
            silinen.delete()
            messages.success(request, 'Ürün sepetten kaldırıldı.')
            return redirect('sepet')
        if 'guncelle' in request.POST:
            urunId = request.POST['urunId']
            sepet = Sepet.objects.get(id = urunId)
            yeniAdet = request.POST['yeniAdet']
            sepet.adet = yeniAdet
            sepet.toplamFiyat = sepet.urun.fiyat * int(yeniAdet)
            sepet.save()
            messages.success(request, 'Sepet güncellendi.')
            return redirect('sepet')

    context = {
        'sepetim':sepetim,
        'toplam':toplam
    }
    return render(request, 'sepet.html', context)

def urundetay(request, urunId):
    urun = Urunler.objects.get(id = urunId)
    context = {
        'urun':urun
    }
    return render(request, 'detay.html', context)