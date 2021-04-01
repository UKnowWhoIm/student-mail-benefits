from datetime import timedelta

from django.utils import timezone
from django.utils.datetime_safe import datetime
from benefits.models import Contribution
from users.models import MailList
from users.utils import invite_as_staff


def send_mails():
    for mail in MailList.objects.filter(mail_sent=False):
        invite_as_staff(mail)


def delete_old_invites():
    threshold = 60 * 60 * 24 * 7  # 7 days
    cutoff_date = timezone.now() - timedelta(seconds=threshold)
    for mail in MailList.objects.filter(last_sent_time__lte=cutoff_date):
        mail.delete()


def delete_old_contributions():
    threshold = 60 * 60 * 24 * 7  # 7 days
    cutoff_date = timezone.now() - timedelta(seconds=threshold)
    for contribution in Contribution.objects.filter(approved=False, timestamp__lte=cutoff_date):
        contribution.delete()


def routine(mail=True, delete_invites=True, delete_contributions=True):
    # Schedule this function daily
    if mail:
        send_mails()
    if delete_invites:
        delete_old_invites()
    if delete_contributions:
        delete_old_contributions()
