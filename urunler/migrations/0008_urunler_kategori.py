# Generated by Django 4.1.5 on 2023-03-23 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0007_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='urunler',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.kategori'),
        ),
    ]