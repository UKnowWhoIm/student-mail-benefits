from django.shortcuts import render
from benefits.models import MailList
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from .forms import CreateUserForm
from .utils import setup_new_user


def create_user(request):
    if request.method == "GET":
        record = MailList.objects.filter(token=request.GET.get("token", ""))
        if record:
            record = record[0]
            form = CreateUserForm(email=record.email)
            return render(request, "users/create_user.html", {"token": record.token, "form": form, "email": record.email})
        return HttpResponseForbidden()
    elif request.method == "POST":
        record = MailList.objects.filter(token=request.POST.get("token", ""))
        if record:
            email = record[0].email
            form = CreateUserForm(data=request.POST)
            if form.is_valid():
                setup_new_user(form.instance, email)
                form.save()
                record.delete()
                return render(request, "users/create_user_success.html", {"email": email})
            return render(request, "users/create_user.html", {"token": request.POST.get("token"), "form": form, "email": record.email})
        return HttpResponseForbidden()
    return HttpResponseBadRequest()
