from django.urls import path
from apps.news import views

urlpatterns = [
    path("", views.GetNews, name="news"),
    path("detail/<int:id>", views.DetailNews, name="detail-news"),
    path("create/", views.CreateNews, name="create-news")
]