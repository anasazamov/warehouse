# Generated by Django 5.0.7 on 2024-08-11 03:34

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('phone', models.CharField(max_length=18, verbose_name='Phone')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Username')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Avatar')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('chat_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='Chat Id on telegram')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'user_table',
            },
        ),
    ]
