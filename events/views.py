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
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event
from events.serializers import EventSerializer


class EventAPIView(APIView, PageNumberPagination):
    allowed_methods = ['get', 'post']
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        quary = request.quary_params.get('quary', '')
        events = Event.objects.filter(Q(title__contains=quary) |
                                       Q(description__contains=quary))
        results = self.paginate_queryset(events, request, view=self)
        return self.get_paginated_response(self.serializer_class(results, many=True).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        date_of_event = request.data.get('date')
        location = request.data.get('location')
        event = Event.objects.create(title=title,
                                      description=description,
                                      date_of_event=date_of_event,
                                      location=location)
        event.save()
        return Response(data=self.serializer_class(event).data,
                        status=status.HTTP_201_CREATED)


class EventDetailAPIView(APIView):
    allowed_methods = ['get', 'put', 'delete']
    serializer_class = EventSerializer

    def get(self, request, id):
        event = Event.objects.get(id=id)
        return Response(data=self.serializer_class(event, many=False).data)

    def put(self, request, id):
        event = Event.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        date_of_event = request.data.get('date')
        location = request.data.get('location')
        event.title = title
        event.description = description
        event.location = location
        event.date_of_event = date_of_event
        event.save()

    def delete(self, request, id):
        event = Event.objects.get(id=id)
        event.delete()
        event = Event.objects.all()
        return Response(data=self.serializer_class(event, many=True).data)
