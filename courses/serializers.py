from rest_framework import serializers

from courses.models import Course, Month


class CourseSerializer(serializers.ModelSerializer):
    month = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = 'id logo title month'

    def get_month(self, obj):
        month = Month.objects.filter(course=obj)
        return MonthSerializer(month, many=True).data


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = 'id number image teacher'.split()
