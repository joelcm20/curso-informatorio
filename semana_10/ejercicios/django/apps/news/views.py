from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsForm
from .models import News

# Create your views here.


def getNews(request):
    if request.method == "POST" and "delete-news" in request.POST:
        user = request.user
        news_id = int(request.POST["delete-news"])
        news = get_object_or_404(News, id=news_id, user=user)
        News.delete(news)

    news = News.objects.all()
    return render(request, "news.html", {"news": news})


def detailNews(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "detail-news.html", {"news": news})


def createNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect("news")
        else:
            return render(request, "create-news.html", {
                "form": NewsForm,
                "error": "Form is not valid!"
            })
    else:
        form = NewsForm()
        return render(request, "create-news.html", {
            "form": form
        })


def deleteNews(request, id):
    if request.method == "POST":
        user = request.user
        news = get_object_or_404(News, id=id, user=user)
        News.delete(news)
        return redirect("news")
