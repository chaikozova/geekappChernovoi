from rest_framework import serializers

from courses.models import Course, Level, Lesson


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = 'id logo title level'.split()

    def get_level(self):
        levels = Level.objects.filter(course=self)
        return LevelSerializer(levels, many=True).data


class LevelSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = 'id title image teacher lessons'.split()

    def get_lessons(self):
        lesson = Lesson.objects.filter(level=self)
        return LessonSerializer(lesson, many=True).data


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = 'id title description'.split()


