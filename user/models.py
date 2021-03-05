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

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя', default=CLIENT)
    username = models.CharField('username', unique=True, max_length=100)
    email = models.EmailField('email', null=True, max_length=100)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    phone = models.CharField('phone', max_length=100)
    telegram = models.CharField('telegram', max_length=200)
    github = models.URLField(max_length=150)
    instagram = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos', max_length=254)
    coins = models.IntegerField()
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']