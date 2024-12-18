# Generated by Django 5.0.8 on 2024-09-05 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_companysettings'),
        ('product', '0009_remove_product_marketplace_type'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productorder',
            unique_together={('product', 'company', 'date', 'warehouse', 'marketplace_type')},
        ),
        migrations.AlterUniqueTogether(
            name='productstock',
            unique_together={('product', 'company', 'date', 'warehouse', 'marketplace_type')},
        ),
    ]
