from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('id','username', 'password','profile', 'nickname')

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
        user.set_password(validated_data['password'])
        user.profile = validated_data.get('profile', user.profile)
        user.nickname = validated_data.get('nickname', user.nickname)
        user.save()
        return user
