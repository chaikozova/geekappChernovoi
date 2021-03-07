from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


ADMIN = 1
TEACHER = 2
MENTOR = 3
STUDENT = 4
CLIENT = 5
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (TEACHER, 'TEACHER'),
    (MENTOR, 'MENTOR'),
    (STUDENT, 'STUDENT'),
    (CLIENT, 'CLIENT'),
)

class Users(AbstractBaseUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя', default=CLIENT)
    username = models.CharField('username', unique=True, max_length=100, blank=True)
    email = models.EmailField('email', null=True, max_length=100, blank=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    phone = models.CharField('phone', max_length=100, blank=True)
    telegram = models.CharField('telegram', max_length=200, blank=True)
    github = models.URLField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='media', max_length=254, blank=True)
    coins = models.IntegerField(blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True, blank=True)
    is_active = models.BooleanField('active', default=True, blank=True)
    is_staff = models.BooleanField(default=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']