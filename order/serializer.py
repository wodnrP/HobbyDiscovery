from rest_framework import serializers
from .models import Order, Order_detail

class OrderSerializer(serializers.ModelSerializer):
    # od_pd = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'o_user', 'o_add', 'o_num', 'o_name', 'o_pay', 'o_total_price', 'o_create')

    # def get_od_pd(self, obj):
    #     od_pd = obj.od_hobby.all()                                                  # obj.(review fk:related name).all()
    #     return Oder_detailSerializer(od_pd, many=True, context=self.context).data

class Order_detailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_detail
        fields = ('id', 'od_id', 'od_pd', 'od_quantity', 'od_price')
        
