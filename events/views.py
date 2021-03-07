# from rest_framework import generics, mixins
# from events.models import Event
# from events.serializers import EventSerializer
#
#
# class EventAPIView(generics.GenericAPIView,
#                    mixins.ListModelMixin,
#                    mixins.CreateModelMixin):
#     serializer_class = EventSerializer
#     queryset = Event.objects.all()
#     lookup_field = 'id'
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class EventDetailAPIView(generics.GenericAPIView,
#                          mixins.RetrieveModelMixin,
#                          mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin):
#     serializer_class = EventSerializer
#     queryset = Event.objects.all()
#     lookup_field = 'id'
#
#     def get(self, request, id=None, **kwargs):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id=None):
#         return self.update(request, id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
