from rest_framework import serializers
from .models import Hobby, review

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('id', 'hobby_name', 'descrition', 'hobby_image') 

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ('title', 'body', 'grade', 'user', 'create_time')
        read_only_fields= ('hobby_id', )