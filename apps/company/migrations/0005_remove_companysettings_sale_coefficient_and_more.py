# Generated by Django 5.0.8 on 2024-09-09 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_delete_countp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companysettings',
            name='sale_coefficient',
        ),
        migrations.AddField(
            model_name='companysettings',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
            preserve_default=False,
        ),
    ]
