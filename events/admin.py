from django.contrib import admin

# Register your models here.
from events.models import Event, Comment, RatingEvent

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(RatingEvent)