# TODO Implement a routine to be executed daily, inviting users asynchronously, and delete old invites
from datetime import timedelta
from django.utils.datetime_safe import datetime
from .models import MailList
from .utils import invite_as_staff


def send_mails():
    for mail in MailList.objects.filter(mail_sent=False):
        invite_as_staff(mail)


def delete_old_invites():
    threshold = 60 * 60 * 24 * 7  # 7 days
    cutoff_date = datetime.now() - timedelta(seconds=threshold)
    for mail in MailList.objects.filter(last_sent_time__lte=cutoff_date):
        mail.delete()


def routine():
    # Schedule this function daily
    send_mails()
    delete_old_invites()
