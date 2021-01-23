from django.core.mail import send_mail, send_mass_mail
from StudentMailBenifits.settings import EMAIL_HOST_USER


def send_email_to_recipient(subject, message, recipient, fail_silently=True):
    send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[recipient],
        fail_silently=fail_silently
    )


def send_email_to_list(subject, message, recipients, fail_silently=True):
    send_mass_mail(
        (subject, message, EMAIL_HOST_USER, recipients),
        fail_silently=fail_silently
    )
