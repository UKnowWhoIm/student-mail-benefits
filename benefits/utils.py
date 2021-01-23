from django.contrib.auth.models import User

from .email import send_email_to_recipient


def get_min_contributions():
    return 2
    # TODO make this a function of number of staff users


def invite_as_staff(email):
    print("SEND MAILLLLLLLLL")
    subject = "Invitation to maintain student benefits"
    body = """
        You are a valuable member of this community. We invite you as a maintainer to student benefits.\n
        As a maintainer, 
        \tAll your contributions are automatically verified.\n
        \tYou can review other contributions made by the community.
    """

    send_email_to_recipient(
        subject=subject,
        message=body,
        recipient=email
    )


def check_promotion(count, email):
    print(count)
    if not User.objects.all().filter(email=email, is_staff=True) and count >= get_min_contributions():
        invite_as_staff(email)
