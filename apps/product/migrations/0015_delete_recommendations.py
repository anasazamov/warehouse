# Generated by Django 5.0.8 on 2024-09-09 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_recommendations_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recommendations',
        ),
    ]