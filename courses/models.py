from django.contrib.postgres.fields import ArrayField
from django.db import models
from users.models import User


class Course(models.Model):
    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'
    logo = models.ImageField(upload_to='media', max_length=240, blank=True, null=True)
    title = models.CharField(max_length=240)
    description = models.TextField(null=True, blank=True)


class Level(models.Model):
    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
    title = models.CharField(max_length=150, null=True)
    teacher = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='teacher')
    image = models.ImageField(upload_to='media',
                              max_length=240, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                               null=True, related_name='level')


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    title = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='lessons')
    video_url = models.URLField(null=True, blank=True)
    material_url = ArrayField(models.CharField(max_length=250,null=True, blank=True), size=5, null=True, blank=True)
