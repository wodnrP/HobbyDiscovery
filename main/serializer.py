from rest_framework import serializers
from .models import Hobby, review, HobbyImage

class HobbyImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = HobbyImage
        fields = ['image']

class HobbySerializer(serializers.ModelSerializer):
    #hobby_image = serializers.ImageField(use_url=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.image.all() 
        return HobbyImageSerializer(image, many=True, context=self.context).data

    class Meta:
        model = Hobby
        fields = ('id', 'hobby_title', 'descrition', 'images') 
    
    def create(self, validated_data):
        instance = Hobby.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            HobbyImage.objects.create(hobby=instance, image=image_data)
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ('title', 'body', 'grade', 'user', 'create_time')
        read_only_fields= ('hobby_id', )