from rest_framework import serializers
from .models import Post, Coments

# serializers의 fields라고 선언해야함.

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'create_time', 'user', 'hits', 'recomend')

class ComentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coments
        fields = ('coment', 'create_time', 'user' )
        read_only_fields= ('post_id', )