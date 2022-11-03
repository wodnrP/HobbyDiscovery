from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import is_valid_path
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import HobbySerializer, ReviewSerializer, RvImageSerializer
from .models import Hobby, Review, Review_Image
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
import math
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from user.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, access_token_exp


# Create your views here.
# Hobby CRUD
# Hobby Gets 전체 게시글 데이터 받아오기 pagenation - 10,최신순, 갯수, 랜덤(가격)
class GetHobby(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 12
        items = request.GET.get('items', None)
        search = request.GET.get('search', None)
        page = request.GET.get('page', None)

        if page is None:
            page = 1

        if search is None:
            search = ""

        if items is not None:
            paginator.page_size = int(items)
        
        page = int(page)

        order_condition = request.GET.get('order', None)
        search_filter = Hobby.objects.filter(pd_title__icontains=search)
        count = search_filter.count()
        page_data = count % paginator.page_size 

        if count <= paginator.page_size:
            total_page = 1

        elif page_data == 0:
            total_page = count / paginator.page_size

        else:
            total_page = count / paginator.page_size + 1
        total_page = math.floor(total_page)
        is_next = total_page - page > 0

        if order_condition == 'pd_price':
            hobby = search_filter.order_by('pd_price')
            result = paginator.paginate_queryset(hobby, request)
        
        elif order_condition == 'review_count':
            hobby = search_filter.annotate(review_count=Count('hobby_rv')).order_by('-review_count')
            result = paginator.paginate_queryset(hobby, request)

        else:
            hobby = search_filter.order_by('pd_create')
            result = paginator.paginate_queryset(hobby, request)
        
        serializer = HobbySerializer(result, many = True, context={"request": request})
        result_serializer = serializer.data
        pagenation = {
            "total_page" : total_page,
            "current_page" : page,
            "total_count" : count,
            "is_next" : is_next,
            "result" : result_serializer
        }
        
        return Response(pagenation, status=status.HTTP_200_OK)

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
    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            review_image = request.GET.get('image', None)
            review_data = {
                "user": id, 
                "title": request.data["title"], 
                "body": request.data["body"], 
                "grade": request.data["grade"],
                "hobby_rv": request.data["hobby_rv"], 
                "image": review_image,
            }
            serializer = ReviewSerializer(data=request.data, partial = True)
            if serializer.is_valid(): 
                serializer.save(data=review_data, request = request)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def patch(self, request, review_id):
        
    #     review = Review.objects.get(pk = review_id)
    #     serializer = ReviewSerializer(review, data=request.data, partial = True)
        
    #     if serializer.is_valid():
    #         serializer.save(data = request.data, request = request)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

