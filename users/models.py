from django.db import models
from django.utils.crypto import get_random_string
from django.utils.datetime_safe import datetime


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
