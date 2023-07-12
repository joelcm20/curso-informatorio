from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import NewsForm

# Create your views here.


def News(request):
    return render(request, "news.html")


def DetailNews(request):
    return render(request, "detail-news.html")


def CreateNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect("news")
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
