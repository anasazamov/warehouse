# Generated by Django 5.0.8 on 2024-09-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_companysettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
