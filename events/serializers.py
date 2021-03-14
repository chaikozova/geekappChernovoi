from rest_framework import serializers
from events.models import Event, Comment, RatingEvent
from user.serializers import UsersSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'created')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment')
        instance.created = validated_data.get('created')
        return instance


class EventSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = ('id', 'image', 'title', 'description', 'created', 'date_of_event', 'location', 'comments')

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        event = Event.objects.create(**validated_data)
        Comment.objects.create(event=event, **comments_data)

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


class RatingEventSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = UsersSerializer(read_only=True)

    class Meta:
        model = RatingEvent
        fields =('id', 'event', 'ratingEvent', 'user')

    def create(self, validated_data):
        return RatingEvent.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.event = validated_data.get('event', instance.event)