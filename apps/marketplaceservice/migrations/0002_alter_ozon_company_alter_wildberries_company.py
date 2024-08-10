# Generated by Django 5.0.7 on 2024-08-10 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('marketplaceservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ozon',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ozon', to='companies.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='wildberries',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wildberries', to='companies.company', verbose_name='Компания'),
        ),
    ]
