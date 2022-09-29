from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ComentsSerializer, PostSerializer
from .models import Post, Coments
from django.contrib.auth.decorators import login_required
from .models import User
from datetime import datetime
#from rest_framework.viewsets import ModelViewSet

from community import serializer
# Create your views here.

# Post CRUD
# Post Gets 전체 게시글 데이터 받아오기 (작성시간 순서)
@api_view(['GET'])
def viewsGetPost(request):
    post = Post.objects.all().order_by('create_time')
    serializer = PostSerializer(post, many = True)
    return Response(serializer.data)

# Post Get 단일 게시글 데이터 받아오기
@api_view(['GET'])
def getPost(request, post_id):
    post = Post.objects.get(pk = post_id)
    serializer = PostSerializer(post, context={"request": request})
    return Response(serializer.data)

# Post Post 게시글 작성하기
@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post Update 단일 게시글 수정 
@api_view(['PATCH'])
def updatePost(request, post_id):
    post = Post.objects.get(pk = post_id)
    serializer = PostSerializer(post, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post DELETE 단일 게시글 삭제 
@api_view(['DELETE'])
def deletePost(request, post_id):
    post = Post.objects.get(pk = post_id)
    post.delete()
    return Response({'message':'sucess', 'code' : 200})


# 게시글 댓글 CRUD
# 해당 글의 댓글 전체 보기 
@api_view(['GET'])
def getComents(request, post_id): 
    coment = Coments.objects.filter(post_id = post_id)
    serializer = ComentsSerializer(coment, many = True)
    return Response(serializer.data)

# 한개의 댓글 보기, 수정, 삭제 
@api_view(['GET', 'PATCH', 'DELETE'])
def  ComentDetail(request, post_id, coment_id): #한 댓글보기, 수정, 삭제
    coment = Coments.objects.get(pk = coment_id)
    if request.method == 'GET':
        serializer = ComentsSerializer(coment)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        print(request.data)
        serializer = ComentsSerializer(coment, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        coment.delete()
        return Response({'message':'sucess', 'code' : 200})

# 댓글 작성
@api_view(['POST'])
def createComent(request, post_id):
    coment = get_object_or_404(Post, pk = post_id)
    serializer = ComentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(post_id = coment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)