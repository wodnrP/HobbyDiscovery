from django.urls import is_valid_path
from requests import request
from rest_framework import serializers
from .models import Subscription, User

class UserSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('id','username', 'password','profile', 'nickname', 'number', 'address')

    def create(self, validated_data):                       # password 해시암호화
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
        # user = super(UserSerializer, self).create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()
        # return user

    def update(self, user, validated_data):
        password = validated_data.get('password', None)
        if password is not None:
            user.set_password(validated_data['password'])
        user.profile = validated_data.get('profile', user.profile)
        user.nickname = validated_data.get('nickname', user.nickname)
        user.number = validated_data.get('number', user.number)
        user.address = validated_data.get('address', user.address)
        user.save()
        return user

class SubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('id', 'user_id', 'create_time', 'delete_time')
        

#use_natural_foreign_key=True