from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)                                                                        # 글 제목
    body = models.TextField()                                                                                       # 글 내용
    create_time = models.DateTimeField(auto_now_add=True)                                                           # 작성된 날짜 및 시간
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, blank=True, null=True)               # 유저정보(외래키) 
    hits = models.PositiveIntegerField(default=0)                                                                   # 조회수
    recomend = models.PositiveIntegerField(default=0)  
    
    def __str__(self):
        return self.title                                                             # 댓글수

# 커뮤니티 게시판 댓글 Model
class Coments(models.Model):
    coment = models.CharField(max_length=100)                                                                       # 댓글 내용
    create_time = models.DateTimeField(auto_now_add=True)                                                           # 댓글 작성 날짜 및 시간
    user = models.ForeignKey("user.User", related_name="comenter", on_delete=models.CASCADE, db_column="user")      # 댓글을 작성한 유저(외래키)
    post_id = models.ForeignKey(Post, related_name="post_num", on_delete=models.CASCADE, db_column="post_id", blank=True, null=True)

    def __str__(self):
        return self.post_id.title