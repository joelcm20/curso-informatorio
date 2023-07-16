from django.urls import path
from . import views

urlpatterns = [
    path("", views.createComment, name="create-comment")
]
