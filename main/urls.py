from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from main.views import reviewViewSet

router = DefaultRouter()
router.register(r'create', views.reviewViewSet)

urlpatterns = [
    path('hobby', views.viewsGetHobby, name="viewsGetHobby"),
    path('<pd_id>', views.getHobby, name="getHobby"),
    path('<hobby_rv>/reviews', views.get_reviews, name="get_reviews"),
    path('<pd_id>/review/<review_id>', views.reviewDetail, name="review_RUD"),
    path('<hobby_rv>/review', views.create_review, name="create_review"),
    #path('create/<pd_id>', views.Create_ReviewView.as_view()),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)