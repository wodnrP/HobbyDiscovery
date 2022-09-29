from django.urls import path, include
from . import views
#from rest_framework.routers import DefaultRouter
#from community.views import PostViewSet
from django.conf import settings


urlpatterns = [
    path('views', views.viewsGetPost, name="viewsGetPost"),
    path('<post_id>', views.getPost, name="getPost"),
    path('create/', views.createPost, name="createPost"), # API가 POST 요청일 때는 url에 ???/ -> /가 포함되어 있어야 함
    path('update/<post_id>', views.updatePost, name="updatePost"),
    path('delete/<int:post_id>', views.deletePost, name="deletePost"),
    path('<post_id>/coments', views.getComents, name="getComents"),
    path('<post_id>/coment', views.createComent, name="createComent"),
    path('<post_id>/coment/<coment_id>', views.ComentDetail, name="readUpdateDelete"),
]   