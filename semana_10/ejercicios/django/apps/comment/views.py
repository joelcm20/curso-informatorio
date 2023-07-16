from django.shortcuts import redirect, get_object_or_404
from apps.news.models import News
from .models import Comment

# Create your views here.


def createComment(request):
    if request.method == "POST":
        news_id = request.POST["news"]
        comment = request.POST["text"]
        news = get_object_or_404(News, id=news_id)
        user = request.user
        Comment.objects.create(news=news, user=user, text=comment)
        return redirect("detail-news", id=news_id)
