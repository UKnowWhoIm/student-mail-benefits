from django.shortcuts import render
from commons.utils import hash_function
from .models import MailList
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from .forms import CreateUserForm
from .utils import pre_save_setup_new_user, post_save_setup_new_user


def create_user(request):
    if request.method == "GET":
        token = hash_function(request.GET.get("token", ""))
        record = MailList.objects.filter(token=token)
        if record:
            record = record[0]
            form = CreateUserForm(email=record.email)
            return render(request, "users/create_user.html", {"token": request.GET["token"],
                                                              "form": form, "email": record.email})
        return HttpResponseForbidden()
    elif request.method == "POST":
        token = hash_function(request.POST.get("token", ""))
        record = MailList.objects.filter(token=token)
        if record:
            email = record[0].email
            form = CreateUserForm(data=request.POST)
            if form.is_valid():
                pre_save_setup_new_user(form.instance, email)
                form.save()
                post_save_setup_new_user(form.instance)
                record.delete()
                return render(request, "users/create_user_success.html", {"email": email})
            return render(request, "users/create_user.html", {"token": token, "form": form, "email": record.email})
        return HttpResponseForbidden()
    return HttpResponseBadRequest()
