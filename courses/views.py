from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseAPIView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CourseDetailAPIView(generics.GenericAPIView,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None, **kwargs):
        return self.retrieve(request, id=id)

    def post(self, request, id=None):
        return self.update(request, id=id)

    def delete(self, request, id=None):
        return self.destroy(request, id=id)