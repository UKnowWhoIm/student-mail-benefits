from django.shortcuts import render
from .models import Category


def new_benefit(request):
    return render(request, "benefits/new.html", {"categories": Category.objects.all()})
