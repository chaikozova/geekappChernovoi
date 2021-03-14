from django.contrib.auth import authenticate
from rest_framework import serializers

from courses.serializers import LevelSerializer, CourseSerializer
from user.models import Users


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(lebel="email", write_only=True)
    password = serializers.CharField(lebel="password",
                                     style={'input_type': 'password'},
                                     write_only=True,
                                     trim_whitespace=False)
    token = serializers.CharField(label='token', read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = 'Unable to login with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = "Must include 'username' and 'password'."
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'phone_number', 'telegram', 'instagram', 'github',
                  'is_staff')


class UserRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'phone_number', 'telegram', 'instagram', 'github',
                  'image')
        read_only_fields = ('created',)


# class TeacherListSerializer(serializers.ModelSerializer):
#     level = LevelSerializer(read_only=True)
#     course = CourseSerializer(read_only=True)
#
#     class Meta:
#         model = Teacher
#         fields = ['id',
#                   'first_name', 'last_name', 'email', 'phone_number', 'email',
#                   'course', 'level']
