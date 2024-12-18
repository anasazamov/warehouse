# Generated by Django 5.0.8 on 2024-09-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_sale_days', models.IntegerField()),
                ('sale_coefficient', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
