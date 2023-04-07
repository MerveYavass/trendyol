from django.forms import ModelForm
from .models import *

class UrunlerForm(ModelForm):
    class Meta:
        model = Urunler
        fields = ['kategori', 'altkategori', 'isim', 'aciklama', 'fiyat', 'resim']

    def __init__(self, *args, **kwargs):
        super(UrunlerForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})