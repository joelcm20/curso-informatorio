from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import NewsForm
from .models import News

# Create your views here.


def GetNews(request):
    news = News.objects.all()
    return render(request, "news.html", {"news": news})


def DetailNews(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "detail-news.html", {"news": news})


def CreateNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
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
