from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError


def Home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })

    if not request.POST["password1"] == request.POST["password2"]:
        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "passwords do not match"
        })

    try:
        user = User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password1"]
        )
        user.save()
        login(request, user)
        return redirect("news")
    except IntegrityError:
        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "user already exists. please try a different username."
        })
