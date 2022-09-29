from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password','profile', 'nickname')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, user, validated_data):
        user.set_password(validated_data['password'])
        user.profile = validated_data.get('profile', user.profile)
        user.nickname = validated_data.get('nickname', user.nickname)
        user.save()
        return user