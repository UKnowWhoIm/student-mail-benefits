import logging

from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

GROUPS = {
    "maintainer": {
        "benefit": ["view"],
        "category": ["view", "add"],
        "contribution": ["view", "add", "change"],
    }
}


class Command(BaseCommand):
    help = "Create the maintainer group"

    def handle(self, *args, **options):
        for group_name in GROUPS.keys():
            new_group, created = Group.objects.get_or_create(name=group_name)

            for app_model in GROUPS[group_name]:
                # Loop permissions in group/model
                for permission_name in GROUPS[group_name][app_model]:

                    # Generate permission name as Django would generate it
                    name = "Can {} {}".format(permission_name, app_model)
                    print("Creating {}".format(name))

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(name))
                        continue

                    new_group.permissions.add(model_add_perm)
