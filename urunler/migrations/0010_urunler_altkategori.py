# Generated by Django 4.1.5 on 2023-03-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0009_altkategori_alter_urunler_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='urunler',
            name='altkategori',
            field=models.ManyToManyField(blank=True, to='urunler.altkategori'),
        ),
    ]