from django.db import models
from user.models import User
from main.models import Hobby

# Create your models here.
class Order(models.Model):
    o_user = models.ForeignKey(User, related_name="order_user", on_delete=models.CASCADE, db_column="user_id")
    o_add = models.TextField()
    o_num = models.CharField(max_length=200)
    o_name = models.CharField(max_length=200)
    o_pay = models.CharField(max_length=100)
    o_total_price = models.IntegerField()

class Order_detail(models.Model):
    od_id = models.ForeignKey("Order", related_name="order", on_delete=models.CASCADE, db_column="od_id")
    od_pd = models.ForeignKey(Hobby, related_name="order_hobby", on_delete=models.CASCADE, db_column="od_hobby")
    od_quantity = models.IntegerField()
    od_price = models.IntegerField()