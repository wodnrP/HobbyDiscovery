from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from main.views import reviewViewSet
from .views import GetHobby

router = DefaultRouter()
router.register(r'create', views.reviewViewSet)

urlpatterns = [
    path('hobby', GetHobby.as_view(), name="viewsGetHobby"),
    path('<pd_id>', views.getHobby, name="getHobby"),
    path('<hobby_rv>/reviews', views.get_reviews, name="get_reviews"),
    path('<pd_id>/review/<review_id>', views.reviewDetail, name="review_RUD"),
    #path('<pd_id>/review', views.create_review, name="create_review"),
    #path('review/', views.CreateReview.as_view()),
    path('<pd_id>/review/', views.review_create, name="review_create"), 
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)