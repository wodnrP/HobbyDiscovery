from rest_framework import serializers
from .models import Order, Order_detail

class OrderSerializer(serializers.ModelSerializer):
    #images = serializers.SerializerMethodField()

    # def get_images(self, obj):
    #     image = obj.rv_image.all()                                                  # obj.(review fk:related name).all()
    #     return RvImageSerializer(image, many=True, context=self.context).data
    
    class Meta:
        model = Order
        # fields = ('id', 'hobby_rv', 'title', 'body', 'grade', 'user', 'create_time', 'update_time', 'images')
        # read_only_fields= ['hobby_rv',]

    # def create(self, instance, **validated_data):
    #     instance = Review.objects.create(**validated_data)
    #     image_set = self.request.FILES.get('image')
    #     for image_data in image_set.getlist('image'):
    #         Review_Image.objects.create(id=instance, image=image_data)
    #     return instance