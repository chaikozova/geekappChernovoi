# Generated by Django 3.1.7 on 2021-03-15 14:01

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, max_length=240, null=True, upload_to='media')),
                ('title', models.CharField(max_length=240)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('image', models.ImageField(blank=True, max_length=240, null=True, upload_to='media')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level', to='courses.course')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Месяц',
                'verbose_name_plural': 'Месяцы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('description', models.TextField(null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('material_url', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), blank=True, null=True, size=5)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level', to='courses.level')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
