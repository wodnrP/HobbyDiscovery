from django.urls import path
from . import views
from .views import SignupAPIView, LoginAPIView, UserAPIView, RefreshAPIView, LogoutAPIView, UserUpdate
urlpatterns = [
    # path('', views.getUsers, name="getUsers"),
    # path('signup', views.signup_view, name='signup'),
    # path('login', views.login_view, name='login'),    
    # path('logout', views.logout_view, name='logout'),
    path('signup', SignupAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('<user_id>', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('update', UserUpdate.as_view()),
    #path('<user_id>', views.userDetail, name="readUpdateDelete"),
]