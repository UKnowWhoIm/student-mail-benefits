import os
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime
from commons.email import send_email_to_recipient
from .models import MailList


def setup_new_user(instance, email):
    maintainer_group = Group.objects.get(name='maintainer')
    instance.email = instance.username = email
    instance.is_staff = True
    instance.groups.add(maintainer_group)


def get_min_contributions():
    return 2  # 10
    # TODO make this a function of number of staff users


def invite_as_staff(email, mail_list_data):

    if not mail_list_data:
        this_data = MailList(email=email)
    else:
        # Wondering why access by index,
        # Refer https://stackoverflow.com/questions/36266172/django-queryset-access-by-index-issue
        this_data = mail_list_data[0]
    this_data.setup()
    link = "http://%s/users/add_user?token=%s" % (os.environ.get("HOST", "localhost:8000"), this_data.token)
    subject = "Invitation to maintain student benefits"
    html_body = render_to_string("email/invite_as_maintainer.html", {'link': link})
    try:
        send_email_to_recipient(
            subject=subject,
            message=html_body,
            recipient=email,
            fail_silently=False
        )

        this_data.save()
    except Exception as e:
        # TODO Log this exception
        print(e)


def check_promotion(count, email):
    diff = 2 * 24 * 60 * 60  # 2 days
    mail_data = MailList.objects.filter(email=email)
    if mail_data and (datetime.now() - mail_data[0].last_sent_time).total_seconds() >= diff or not mail_data:
        if not User.objects.filter(username=email, is_staff=True) and count >= get_min_contributions():
            invite_as_staff(email, mail_data)
