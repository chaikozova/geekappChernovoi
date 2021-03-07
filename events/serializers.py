# from rest_framework import serializers
#
# from events.models import Event, Comment
#
#
# class EventSerializer(serializers.ModelSerializer):
#     comments = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Event
#         fields = 'id image title description created comments'.split()
#
#     def get_comments(self, obj):
#         comments = Comment.objects.filter(event=obj)
#         return CommentSerializer(comments,
#                                  many=True).data
#
#
# class CommentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Comment
#         fields = 'id comment created'.split()
