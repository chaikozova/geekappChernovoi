from django.contrib import admin

# Register your models here.
from courses.models import Course, Level, Lesson

admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Lesson)
