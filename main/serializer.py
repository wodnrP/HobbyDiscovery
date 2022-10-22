from rest_framework import serializers
from .models import Hobby, Review, HobbyImage, Review_Image

class HobbyImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    pd_image = serializers.ImageField(use_url=True)
    class Meta:
        model = HobbyImage
        fields = ['image', 'pd_image']

class HobbySerializer(serializers.ModelSerializer):
    #hobby_image = serializers.ImageField(use_url=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.image.all() 
        return HobbyImageSerializer(image, many=True, context=self.context).data

    def get_pd_images(self, obj):
        pd_image = obj.image.all() 
        return HobbyImageSerializer(pd_image, many=True, context=self.context).data
    
    class Meta:
        model = Hobby
        fields = ('pd_id', 'pd_title', 'pd_descrition', 'pd_info', 'pd_price', 'pd_sell', 'pd_create', 'images') 
    
    def create(self, validated_data):
        instance = Hobby.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            HobbyImage.objects.create(id=instance, image=image_data)
        return instance


class RvImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Review_Image
        fields = ['image']

class ReviewSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.rv_image.all()                                                  # obj.(review fk:related name).all()
        return RvImageSerializer(image, many=True, context=self.context).data
    
    class Meta:
        model = Review
        fields = ('id', 'hobby_rv', 'title', 'body', 'grade', 'user', 'create_time', 'update_time', 'images')
        read_only_fields= ['hobby_rv',]

    def create(self, validated_data):
        instance = Review.objects.create(**validated_data)
        print(instance)
        image_set = self.request.FILES.get('image')
        print(3)
        for image_data in image_set.getlist('image'):
            Review_Image.objects.create(id=instance, image=image_data)
        return instance


