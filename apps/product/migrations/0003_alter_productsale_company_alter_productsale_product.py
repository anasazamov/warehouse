# Generated by Django 5.0.8 on 2024-08-12 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('product', '0002_remove_ozonproductsales_ozon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsale',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sales', to='company.company'),
        ),
        migrations.AlterField(
            model_name='productsale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='product.product'),
        ),
    ]