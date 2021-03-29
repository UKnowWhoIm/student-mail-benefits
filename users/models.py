from django.db import models
from django.utils.crypto import get_random_string
from django.utils.datetime_safe import datetime
from commons.utils import hash_function


class MailList(models.Model):
    email = models.EmailField(unique=True)
    last_sent_time = models.DateTimeField(null=True, default=None)
    token = models.CharField(max_length=1000, unique=True, null=True)
    mail_sent = models.BooleanField(default=False)

    def setup(self):
        self.last_sent_time = datetime.now()
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_."
        # Make token unique
        all_tokens = [i.token for i in MailList.objects.all()]
        _current_token = get_random_string(64, chars)
        current_token = hash_function(_current_token)
        while current_token in all_tokens:
            _current_token = get_random_string(64, chars)
            current_token = hash_function(_current_token)

        self.token = current_token
        return _current_token
