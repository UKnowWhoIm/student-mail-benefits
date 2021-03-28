from django.core.management import BaseCommand
from users.routine import send_mails


class Command(BaseCommand):
    help = "Send pending invite emails"

    def handle(self, *args, **options):
        send_mails()
