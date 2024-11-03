# Generated by Django 5.0.8 on 2024-09-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_alter_inproduction_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendations',
            name='days_left',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
