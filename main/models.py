from django.db import models
import user
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# 취미 Model
class Hobby(models.Model):
    pd_id = models.AutoField(primary_key=True)
    pd_title = models.CharField(max_length=100)                                                                   # 취미 이름
    pd_descrition = models.TextField()                                                                             # 취미 설명 내용
    pd_info = models.TextField(blank=True, null=True)
    pd_price = models.IntegerField()
    pd_sell = models.CharField(max_length=100, blank=True, null=True)
    pd_create = models.DateTimeField(auto_now_add=True)                                                                                                                                                 # 취미관련 이미지
    
    def __str__(self):
        return self.pd_title            

# 취미 image 업로드 경로
def image_upload_path(instance, filename):
    print('success')
    return f'{instance}/{filename}'

class HobbyImage(models.Model):
    id = models.AutoField(primary_key=True)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=image_upload_path)
    pd_image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    def __str__(self):
        return self.hobby.pd_title

    class Meta:
        db_table = 'hobby_image'                                                       

# 후기 모음집 Model
class Review(models.Model):
    title = models.CharField(max_length=200)                                                                        # 후기 제목
    body = models.TextField()                                                                                       # 후기 내용
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(null=True, auto_now=True)                                                          # 후기가 작성된 날짜 및 시간
    grade = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])         # 후기 평점 최소 0, 최대 5까지 값 받도록 지정
    user = models.ForeignKey("user.User", related_name="reviewer", on_delete=models.CASCADE, db_column="user")      # 후기를 작성한 유저(외래키)
    hobby_rv = models.ForeignKey("Hobby", related_name="hobby_rv", on_delete=models.CASCADE, db_column="hobby_rv", blank=True, null=False)      # 해당 취미 (외래키)
    def __str__(self):
        return self.hobby_rv.pd_title

class Review_Image(models.Model):
    id = models.AutoField(primary_key=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rv_image')
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    def __str__(self):
        return self.reviews.title

    class Meta:
        db_table = 'review_image'