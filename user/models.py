from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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


class Users(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, default=CLIENT, verbose_name='Тип пользователя')
    email = models.EmailField(max_length=250, unique=True, db_index=True, verbose_name='Email')
    username = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='Username')
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='First name')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last name')
    phone_number = models.CharField(max_length=200, blank=True, null=True, verbose_name='Phone number')
    telegram = models.CharField(max_length=200, blank=True, null=True, verbose_name='Telegram')
    github = models.URLField(max_length=150, blank=True, null=True, verbose_name='Github')
    instagram = models.CharField(max_length=150, blank=True, null=True, verbose_name='Instagram')
    image = models.ImageField(upload_to='media', max_length=254, blank=True)
    coins = models.IntegerField(blank=True, null=True, verbose_name='Geek coins')
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Date of join')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    is_staff = models.BooleanField(default=False, verbose_name='Is staff')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


# class Teacher(Users):
#     class Meta:
#         verbose_name = 'Учитель'
#         verbose_name_plural = 'Учителя'
#
#     level = models.ForeignKey(Level, on_delete=models.SET_NULL,
#                               null=True,
#                               related_name='level')
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL,
#                                null=True, related_name='course')
#
#     def __str__(self):
#         return self.first_name + ' - '+self.course.title + ' / '+self.level.title


@receiver(post_save)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if issubclass(sender, Users) and created:
        Token.objects.create(user=instance)
