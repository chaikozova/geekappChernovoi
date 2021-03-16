from rest_framework import generics, mixins

from courses.models import Course, Level, Lesson
from courses.serializers import CourseSerializer, LevelSerializer, LessonSerializer


class CourseAPIView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseDetailAPIView(generics.GenericAPIView,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LevelAPIView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LevelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = "id"


class LessonAPIView(generics.ListCreateAPIView):
    """
    List of lessons in 1 month
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()