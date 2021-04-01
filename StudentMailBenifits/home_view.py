from django.shortcuts import render


def home_view(r):
    return render(r, "common/home.html")
