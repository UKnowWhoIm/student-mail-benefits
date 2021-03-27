from django.utils.crypto import get_random_string
from django.db import models
from django.utils.datetime_safe import datetime


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Benefit(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, related_name="benefits", on_delete=models.SET_NULL, null=True)
    highlights = models.JSONField(default=list)
    link = models.CharField(max_length=100)
    img_file = models.CharField(max_length=2048, blank=True)

    @property
    def contributors(self):
        return [i.email for i in self.contribution_set.filter(approved=True) if i.email]

    def __str__(self):
        return self.title


class Contribution(models.Model):
    email = models.EmailField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    contribution = models.JSONField()
    benefit = models.ForeignKey(Benefit, on_delete=models.SET_NULL, null=True, rel="contributions", blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        if self.benefit:
            return self.benefit.title
        return self.contribution["title"]


class MailList(models.Model):
    email = models.EmailField(unique=True)
    last_sent_time = models.DateTimeField()
    token = models.CharField(max_length=64, unique=True, null=True)

    def setup(self):
        self.last_sent_time = datetime.now()
        # TODO hash token
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_."
        # Make token unique
        all_tokens = [i.token for i in MailList.objects.all()]
        current_token = get_random_string(64, chars)
        while current_token in all_tokens:
            current_token = get_random_string(64, chars)

        self.token = current_token
