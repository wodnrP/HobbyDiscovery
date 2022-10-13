from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hobby', views.viewsGetHobby, name="viewsGetHobby"),
    path('<hobby_id>', views.getHobby, name="getHobby"),
    path('reviews', views.get_reviews, name="get_reviews"),
    path('<hobby_id>/review/<review_id>', views.reviewDetail, name="review_RUD"),
    path('<hobby_id>/review', views.create_review, name="create_review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)