# Generated by Django 5.0.8 on 2024-09-22 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_companysettings_next_sale_days'),
        ('product', '0031_recomamandationsupplier'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recommendations',
            unique_together={('company', 'product')},
        ),
    ]