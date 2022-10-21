from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(null=True, blank=True)                         # 유저 프로필 이미지
    nickname = models.CharField(max_length=100, unique = True, null=True)      # 유저 닉네임 
    number = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class Subscription(models.Model):
    user_id = models.ForeignKey(User, related_name="user_sub", on_delete=models.CASCADE, db_column="user_id")
    create_time = models.DateTimeField(auto_now_add=True)
    delete_time = models.DateTimeField()

