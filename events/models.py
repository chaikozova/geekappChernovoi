from django.db import models


class Event(models.Model):
    image = models.ImageField(upload_to='media', max_length=240)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def view_comments(self):
        return Comment.objects.filter(comments=self)


class Comment(models.Model):
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)
    rate = models.DecimalField(max_digits=5, decimal_places=1, default=1)
    events = models.ForeignKey(Event,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='comments')
