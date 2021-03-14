from rest_framework import serializers

from user.models import Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

    # def create(self, validated_data):
    #     return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.github = validated_data.get('github', instance.github)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.image = validated_data.get('image', instance.image)
        return instance