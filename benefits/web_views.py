from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .models import Category, Benefit


def new_benefit(request, benefit=None):
    return render(request, "benefits/form.html", {"categories": Category.objects.all(), "benefit": benefit})


def edit_benefit(request, benefit_id=None):
    if benefit_id:
        benefit = Benefit.objects.filter(id=benefit_id)
        if benefit:
            return new_benefit(request, benefit[0])
        return HttpResponseBadRequest()
    return render(request, "benefits/edit.html")

