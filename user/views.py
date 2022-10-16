from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, access_token_exp
from .serializer import UserSerializer
from .models import User

# Create your views here.
# @api_view(['GET'])                                                                  # 전체 유저 조회
# def getUsers(request):                                                             
#     users = User.objects.all()
#     serializer = UserSerializer(users, many = True)
#     return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])                                               # 단일 회원 조회, 수정, 삭제
def userDetail(request, user_id): 
    user = User.objects.get(pk = user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message':'sucess', 'code' : 200})

# @api_view(['POST'])                                                                  # 회원가입
# def signup_view(request): 
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])                                                                  # 로그인
# def login_view(request): 
#     serializer = UserSerializer(data=request.data)
#     username = serializer.initial_data['username']
#     password = serializer.initial_data['password']
#     user = authenticate(request=request, username=username, password=password)
#     token = Token.objects.get(user=user)
#     if user is not None:
#         login(request, user)
#         return Response(serializer.initial_data, {"Token" : token.key}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def logout_view(request):                                                            # 로그아웃
#     logout(request)
#     return redirect('getUsers')

class MyNotFoundException(APIException):
    status_code = 400
    default_detail = '로그인 실패 다시 확인해주세요'
    default_code = 'KeyNotFound'

class SignupException(APIException):
    status_code = 400
    default_detail = '아이디 혹은 패스워드를 다시 확인해주세요'
    default_code = 'KeynotFound'

class SignupAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
            user = User.objects.filter(username=request.data['username']).first()
            if not user:
                raise SignupException()
            if not user.check_password(request.data['password']):
                raise SignupException()

            access_token = create_access_token(user.id)
            access_exp = access_token_exp(access_token)             
            refresh_token = create_refresh_token(user.id)
            #serializer_data = serializer.data

            response = Response()
            response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
            response.data = {
                #'serializer_data' : serializer_data,
                'access_token' : access_token,              
                'access_exp' : access_exp,                  
                'refresh_token' : refresh_token         
            }
            return response

class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(username=request.data['username']).first()
        
        if not user:
            raise MyNotFoundException()
        if not user.check_password(request.data['password']):
            raise MyNotFoundException()

        access_token = create_access_token(user.id)
        access_exp = access_token_exp(access_token)     # 생성된 access token의 decode된 만료기간 생성
        refresh_token = create_refresh_token(user.id)

        response = Response()
        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'access_token' : access_token,              # access token 반환
            'access_exp' : access_exp,                  # access 만료기간 반환
            'refresh_token' : refresh_token             # refresh token 반환
            }
        return response


class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()
            return Response(UserSerializer(user).data)
        
        raise AuthenticationFailed('unauthenticated')

class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })

class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }

        return response

