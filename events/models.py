from django.db import models

from user.models import Users


class Event(models.Model):
    class Meta:
        verbose_name = 'Меропрятие'
        verbose_name_plural = 'Меропрятия'
    image = models.ImageField(upload_to='media', max_length=240, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    date_of_event = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def view_comments(self):
        return Comment.objects.filter(comments=self)

    def get_ratings(self):
        return RatingEvent.objects.filter(event=self)


class Comment(models.Model):
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)
    rate = models.DecimalField(max_digits=5,
                               decimal_places=1,
                               default=1)
    events = models.ForeignKey(Event,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='comments')


class RatingEvent(models.Model):
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = [
            'user',
            'event']
    SCORE_CHOICES = zip(range(1,6), range(1,6))
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event')
    ratingEvent = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, blank=True)

    def __str__(self):
        return 'Rating(Event =' + str(self.event) + ', Stars =' + str(self.ratingEvent) + ')'
