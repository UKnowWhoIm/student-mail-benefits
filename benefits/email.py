from django.core.mail import send_mail, send_mass_mail
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from StudentMailBenifits.settings import EMAIL_HOST_USER


def send_email_to_recipient(subject, message, recipient, fail_silently=True):
    # message is in html
    message = EmailMessage(subject=subject, body=message, from_email=EMAIL_HOST_USER, to=[recipient])
    message.content_subtype = "html"
    message.send(fail_silently)


def send_email_to_list(subject, message, recipients, fail_silently=True):
    # message is in html
    send_mass_mail(
        (subject, message, EMAIL_HOST_USER, recipients),
        fail_silently=fail_silently
    )
