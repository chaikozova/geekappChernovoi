from django.contrib.postgres.fields import ArrayField
from django.db import models
from user.models import Users


class Course(models.Model):
    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'
    logo = models.ImageField(upload_to='media', max_length=240)
    title = models.CharField(max_length=240)
    months = ArrayField(
        ArrayField(
            models.CharField(max_length=15,
                             blank=True),
            size=9), size=9)


class Month(models.Model):
    number = models.IntegerField()
    teacher = models.ForeignKey(Users,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='teacher')
    image = models.ImageField(upload_to='media',
                              max_length=240)
