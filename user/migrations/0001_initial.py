# Generated by Django 3.1.7 on 2021-03-06 11:58

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_type', models.IntegerField(choices=[(1, 'ADMIN'), (2, 'TEACHER'), (3, 'MENTOR'), (4, 'STUDENT'), (5, 'CLIENT')], default=5, verbose_name='Тип пользователя')),
                ('username', models.CharField(blank=True, max_length=100, unique=True, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='phone')),
                ('telegram', models.CharField(blank=True, max_length=200, verbose_name='telegram')),
                ('github', models.URLField(blank=True, max_length=150)),
                ('instagram', models.CharField(blank=True, max_length=150)),
                ('image', models.ImageField(blank=True, max_length=254, upload_to='photos')),
                ('coins', models.IntegerField(blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
