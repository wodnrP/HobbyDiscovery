from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ImageField
import order
# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(null=True, blank=True)                         # 유저 프로필 이미지
    nickname = models.CharField(max_length=100, unique = True, null=True)      # 유저 닉네임 
    number = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class Subscription(models.Model):
    user_id = models.ForeignKey(User, related_name="user_sub", on_delete=models.CASCADE, db_column="user_id")
    create_time = models.DateTimeField(auto_now_add=True)
    delete_time = models.DateTimeField(null=True)
    subpd_id = models.ForeignKey("Sub_pd", related_name="sub_product", on_delete=models.CASCADE, db_column="subpd_id", null=True)
    order_id = models.ForeignKey("order.Order", related_name="sub_order", on_delete=models.CASCADE, db_column="order_id", null=True)

class Sub_pd(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    price = models.IntegerField()
    sub_image = models.ImageField()
