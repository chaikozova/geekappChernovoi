from django.contrib import admin


# Register your models here.
from user.models import Users

admin.site.register(Users)
# admin.site.register(Teacher)