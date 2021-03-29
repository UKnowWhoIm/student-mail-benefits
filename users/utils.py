import os
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from django.utils import timezone
from commons.email import send_email_to_recipient
from .models import MailList


def setup_new_user(instance, email):
    maintainer_group = Group.objects.get(name='maintainer')
    instance.email = instance.username = email
    instance.is_staff = True
    instance.groups.add(maintainer_group)


def get_min_contributions():
    count = len(User.objects.filter(is_staff=True, is_active=True))
    return max(int(1.3 ** count), 10)


def invite_as_staff(mail_data):
    email = mail_data.email

    token = mail_data.setup()
    link = "http://%s/users/add_user?token=%s" % (os.environ.get("HOST", "localhost:8000"), token)
    subject = "Invitation to maintain student benefits"
    html_body = render_to_string("email/invite_as_maintainer.html", {'link': link})
    try:
        send_email_to_recipient(
            subject=subject,
            message=html_body,
            recipient=email,
            fail_silently=False
        )
        mail_data.last_sent_time = timezone.now()
        mail_data.mail_sent = True
        mail_data.save()
    except Exception as e:
        # TODO Log this exception
        print(e)


def check_promotion(count, email):
    diff = 2 * 24 * 60 * 60  # 2 days
    mail_data = MailList.objects.filter(email=email)
    if mail_data and (datetime.now() - mail_data[0].last_sent_time).total_seconds() >= diff or not mail_data:
        if not User.objects.filter(username=email, is_staff=True) and count >= get_min_contributions():
            if mail_data:
                mail_data.delete()
            MailList.objects.create(email=email)
