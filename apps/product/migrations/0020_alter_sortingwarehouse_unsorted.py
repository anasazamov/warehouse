# Generated by Django 5.0.8 on 2024-09-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_shelf_sortingwarehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortingwarehouse',
            name='unsorted',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
