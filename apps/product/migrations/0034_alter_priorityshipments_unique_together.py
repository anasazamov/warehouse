# Generated by Django 5.0.8 on 2024-09-24 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_companysettings_next_sale_days'),
        ('product', '0033_priorityshipments'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='priorityshipments',
            unique_together={('company', 'warehouse', 'marketplace_type')},
        ),
    ]
