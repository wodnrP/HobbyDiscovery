from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import OrderAPIView, Order_detailAPIView

urlpatterns = [
    path('', OrderAPIView.as_view()),
    path('detail', Order_detailAPIView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)