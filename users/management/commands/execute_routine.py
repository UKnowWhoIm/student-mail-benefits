from django.core.management import BaseCommand
from commons.routine import routine


class Command(BaseCommand):
    help = "Execute the daily routine to clear outdated invites and contributions and send mails"

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-email",
            help="Do not send emails",
            action="store_true"
        )
        parser.add_argument(
            "--no-invites",
            help="Do not delete old invites",
            action="store_true"
        )
        parser.add_argument(
            "--no-contributions",
            help="Do not delete old contributions",
            action="store_true"
        )

    def handle(self, *args, **options):
        routine(mail=not options["no_email"],
                delete_invites=not options["no_invites"], delete_contributions=not options["no_contributions"])

