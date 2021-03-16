from decimal import Decimal

from django.db.models import Avg
from rest_framework import serializers
from events.models import Event, Comment


class CommentSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'rate', 'created', 'events')

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        event = Event.objects.get()
        avg = Comment.objects.all().aggregate(Avg('rate'))
        print(avg)
        event.ratting = Decimal(avg['rate__avg'])
        event.save()
        return comment

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment')
        instance.created = validated_data.get('created')
        return instance


class EventSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = ('id', 'image', 'title', 'description', 'ratting', 'created', 'date_of_event', 'location', 'comments')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments')
        comments = instance.comments

        instance.image = validated_data.get('image')
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.created = validated_data.get('created')
        instance.date_of_event = validated_data.get('date_of_event')
        instance.location = validated_data.get('location')
        instance.save()
        for comments_data in comments_data:
            comment = comments.pop(0)
            comment.comment = comments_data.get('comment')
            comment.created = comments_data.get('created')
            comment.save()
        return instance
