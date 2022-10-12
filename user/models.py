from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(null=True, blank=True)                         # 유저 프로필 이미지
    nickname = models.CharField(max_length=100, unique = True, null=True)      # 유저 닉네임 