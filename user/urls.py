from django.urls import path
from . import views
from .views import SignupAPIView, LoginAPIView, UserAPIView, RefreshAPIView, LogoutAPIView, SubscriptionAPIView, Sub_pdAPIView
urlpatterns = [
    # path('', views.getUsers, name="getUsers"),
    # path('signup', views.signup_view, name='signup'),
    # path('login', views.login_view, name='login'),    
    # path('logout', views.logout_view, name='logout'),
    path('signup', SignupAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('', UserAPIView.as_view()),
    path('<int:user_id>', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    #path('sub/', SubAPIView.as_view()),
    path('sub', SubscriptionAPIView.as_view()),
    path('sub_pd', Sub_pdAPIView.as_view()),
    #path('update', UserUpdate.as_view()),
]