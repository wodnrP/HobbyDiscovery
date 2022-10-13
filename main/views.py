from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import HobbySerializer, ReviewSerializer
from .models import Hobby, review

# Create your views here.
# Hobby CRUD
# Hobby Gets 전체 게시글 데이터 받아오기
@api_view(['GET'])
def viewsGetHobby(request):
    hobby = Hobby.objects.all()
    serializer = HobbySerializer(hobby, many = True, context={"request": request})
    return Response(serializer.data)

# Hobby Get 단일 게시글 데이터 받아오기
@api_view(['GET'])
def getHobby(request, hobby_id):
    hobby = Hobby.objects.get(pk = hobby_id)
    serializer = HobbySerializer(hobby, context={"request": request})
    return Response(serializer.data)

# review CRUD
# 전체 review 데이터 불러오기 
@api_view(['GET'])
def get_reviews(request):
    reviews = review.objects.all()
    serializer = ReviewSerializer(reviews, many = True)
    return Response(serializer.data) 

# 한개의 리뷰 보기, 수정, 삭제 
@api_view(['GET', 'PATCH', 'DELETE'])
def  reviewDetail(request, review_id, hobby_id):
    review = review.objects.get(pk = review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        print(request.data)
        serializer = ReviewSerializer(review, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        return Response({'message':'sucess', 'code' : 200})

# 리뷰 작성 기능 
@api_view(['POST'])
def create_review(request, hobby_id):
    review = get_object_or_404(Hobby, pk = hobby_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(hobby_id = review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)