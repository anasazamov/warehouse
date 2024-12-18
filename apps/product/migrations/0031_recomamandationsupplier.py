# Generated by Django 5.0.8 on 2024-09-22 16:37

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_companysettings_next_sale_days'),
        ('product', '0030_alter_inproduction_recommendations'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecomamandationSupplier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('days_left', models.IntegerField(default=0)),
                ('marketplace_type', models.CharField(choices=[('wildberries', 'Wildberries'), ('ozon', 'Ozon'), ('yandexmarket', 'YandexMarket')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.warehouse')),
            ],
        ),
    ]
