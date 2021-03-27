import os
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from .email import send_email_to_recipient
from .models import MailList


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
    body = """
        <h3>You are a valuable member of this community. We invite you as a maintainer to student benefits</h3>.\n
        As a maintainer, 
        \t - All your contributions are automatically verified.
        \t - You can review other contributions made by the community.
        
        <a href=\'%s\'>Click Here</a> to become a maintainer.
        Copy paste this url to your browser if this doesn't work: %s 
    """ % (link, link)
    try:
        send_email_to_recipient(
            subject=subject,
            message=body,
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
        if not User.objects.filter(email=email, is_staff=True) and count >= get_min_contributions():
            invite_as_staff(email, mail_data)
