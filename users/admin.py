from django.contrib import admin

# Register your models here.
from users.models import MailList

admin.site.register(MailList)
