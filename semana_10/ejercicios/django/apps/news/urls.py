from django.urls import path
from apps.news import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.News, name="news"),
    path("detail/", views.DetailNews, name="detail-news"),
    path("create/", views.CreateNews, name="create-news")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
