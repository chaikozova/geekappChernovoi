# Generated by Django 3.1.7 on 2021-03-14 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210314_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level', to='courses.course'),
        ),
    ]