# Generated by Django 4.1.5 on 2023-03-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('aciklama', models.TextField(max_length=1000)),
                ('fiyat', models.IntegerField()),
            ],
        ),
    ]
