from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import GetHobby, CreateReview



urlpatterns = [
    path('hobby', GetHobby.as_view(), name="viewsGetHobby"),
    path('<int:pd_id>', views.getHobby, name="getHobby"),
    path('<int:hobby_rv>/reviews', views.get_reviews, name="get_reviews"),
    path('<int:pd_id>/review/<int:review_id>', views.reviewDetail, name="review_RUD"),
    path('review/<int:review_id>', views.CreateReview.as_view()),
    path('review/', views.CreateReview.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)