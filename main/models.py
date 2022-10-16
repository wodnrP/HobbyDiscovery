from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# 취미 Model
class Hobby(models.Model):
    hobby_title = models.CharField(max_length=50)                                                                   # 취미 이름
    descrition = models.TextField()                                                                                 # 취미 설명 내용
    hobby_image = models.ImageField(blank=True, upload_to="")                                                                     # 취미관련 이미지
    
    def __str__(self):
        return self.hobby_title                                                                    

# 후기 모음집 Model
class review(models.Model):
    title = models.CharField(max_length=200)                                                                        # 후기 제목
    body = models.TextField()                                                                                       # 후기 내용
    create_time = models.DateTimeField(auto_now_add=True)                                                           # 후기가 작성된 날짜 및 시간
    grade = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])         # 후기 평점 최소 0, 최대 5까지 값 받도록 지정
    user = models.ForeignKey("user.User", related_name="reviewer", on_delete=models.CASCADE, db_column="user")      # 후기를 작성한 유저(외래키)
    hobby_id = models.ForeignKey(Hobby, related_name="hobbys", on_delete=models.CASCADE, db_column="hobby_id")      # 해당 취미 (외래키)
    
    def __str__(self):
        return self.hobby_id.hobby_title    