from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import GetHobby, CreateReview



urlpatterns = [
    path('hobby', GetHobby.as_view(), name="viewsGetHobby"),
    path('hobby/<int:pd_id>', views.getHobby, name="getHobby"),
    path('reviews/<int:hobby_rv>', views.get_reviews, name="get_reviews"),
    path('review/<int:pd_id>/<int:review_id>', views.reviewDetail, name="review_RUD"),
    path('review/<int:review_id>', views.CreateReview.as_view()),
    path('review/', views.CreateReview.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)