# Generated by Django 5.0.7 on 2024-08-11 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('marketplaceservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Уникальный идентификатор')),
                ('place_in_warehouse', models.CharField(blank=True, max_length=500, null=True, verbose_name='Местонахождение на складе')),
                ('ozon_vendor_code', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Озон Яндекс.Маркета')),
                ('ozon_barcode', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Штрих-код Ozon')),
                ('ozon_product_id', models.CharField(blank=True, max_length=1000, null=True, verbose_name='ID продукта Ozon')),
                ('ozon_sku', models.CharField(blank=True, max_length=1000, null=True, verbose_name='SKU Ozon')),
                ('ozon_fbo_sku_id', models.CharField(blank=True, max_length=1000, null=True, verbose_name='ID SKU FBO Ozon')),
                ('ozon_fbs_sku_id', models.CharField(blank=True, max_length=1000, null=True, verbose_name='ID SKU FBS Ozon')),
                ('yandex_vendor_code', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Артикул Яндекс.Маркета')),
                ('yandex_barcode', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Штрих-код Яндекс.Маркета')),
                ('yandex_sku', models.CharField(blank=True, max_length=1000, null=True, verbose_name='SKU Яндекс.Маркета')),
                ('willberries_vendor_code', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Артикул Willberries')),
                ('willberries_barcode', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Штрих-код Willberries')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProductCompany', to='companies.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'product_table',
            },
        ),
        migrations.CreateModel(
            name='OzonProductSales',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Уникальный идентификатор')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество проданных товаров')),
                ('remain_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Остаток товаров')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(verbose_name='Дата обновления')),
                ('ozon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OzonProduct', to='marketplaceservice.ozon', verbose_name='Ozon')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OzonProduct', to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продажи на Ozon',
                'verbose_name_plural': 'Продажи на Ozon',
                'db_table': 'ozon_product_table',
            },
        ),
        migrations.CreateModel(
            name='InProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_to_produce_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Необходимо произвести')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(verbose_name='Дата обновления')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='InProductionProduct', to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'В производстве',
                'verbose_name_plural': 'В производстве',
                'db_table': 'in_production_product_table',
            },
        ),
        migrations.CreateModel(
            name='WildberriesProductSales',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Уникальный идентификатор')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество проданных товаров')),
                ('remain_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Остаток товаров')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(verbose_name='Дата обновления')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='WildberriesProduct', to='products.product', verbose_name='Продукт')),
                ('wildberries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='WildberriesProduct', to='marketplaceservice.wildberries', verbose_name='Wildberries')),
            ],
            options={
                'verbose_name': 'Продажи на Wildberries',
                'verbose_name_plural': 'Продажи на Wildberries',
                'db_table': 'wildberries_product_table',
            },
        ),
        migrations.CreateModel(
            name='YandexMarketProductSales',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Уникальный идентификатор')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество проданных товаров')),
                ('remain_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Остаток товаров')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(verbose_name='Дата обновления')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='YandexMarketProduct', to='products.product', verbose_name='Продукт')),
                ('yandex_market', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='YandexMarketProduct', to='marketplaceservice.yandexmarket', verbose_name='YandexMarket')),
            ],
            options={
                'verbose_name': 'Продажи на YandexMarket',
                'verbose_name_plural': 'Продажи на YandexMarket',
                'db_table': 'yandex_market_product_table',
            },
        ),
    ]
