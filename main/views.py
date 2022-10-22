from urllib import response
from django.shortcuts import render, get_object_or_404
from django.urls import is_valid_path
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import HobbySerializer, ReviewSerializer
from .models import Hobby, Review

# Create your views here.
# Hobby CRUD
# Hobby Gets 전체 게시글 데이터 받아오기
@api_view(['GET'])
def viewsGetHobby(request):
    hobby = Hobby.objects.all()
    serializer = HobbySerializer(hobby, many = True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)

# Hobby Get 단일 게시글 데이터 받아오기
@api_view(['GET'])
def getHobby(request, pd_id):
    hobby = Hobby.objects.get(pk = pd_id)
    serializer = HobbySerializer(hobby, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)

# review CRUD
# 전체 review 데이터 불러오기 
@api_view(['GET'])
def get_reviews(request, hobby_rv):
    reviews = Review.objects.filter( hobby_rv = hobby_rv)
    print(reviews)
    serializer = ReviewSerializer(reviews, many = True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)

# 한개의 리뷰 보기, 수정, 삭제 
@api_view(['GET', 'PATCH', 'DELETE'])
def  reviewDetail(request, review_id, pd_id):
    reviews = Review.objects.get(pk = review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        print(request.data)
        serializer = ReviewSerializer(reviews, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        reviews.delete()
        return Response({'message':'sucess', 'code' : 200})

#리뷰 작성 기능 
class CreateReview(APIView):
    def post(request, *data, **pd_id):
        review = get_object_or_404(Hobby, pk = pd_id).filter
        print(review)
        serializer = ReviewSerializer(data=request.data)
        print('s',serializer)
        if serializer.is_valid():
            serializer.save(pd_id = review)
            print(2)
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class reviewViewSet(ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = ReviewSerializer

    def pre_save(self, obj):
        print(1)
        obj.samplesheet = self.request.FILES.get('image')
    
#     def create(self, request, pd_id):
#         reviews = Hobby.objects.get(pk=pd_id)
#         serializer = ReviewSerializer(data=request.data) 
#         print(reviews)
#         if serializer.is_valid():
#             serializer.save(pd_id = reviews)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)