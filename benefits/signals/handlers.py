from django.db.models.signals import post_save
from django.dispatch import receiver
from benefits.models import Contribution, Benefit
from benefits.utils import check_promotion


@receiver(post_save, sender=Contribution)
def make_contribution(sender, instance, created, **kwargs):
    if instance.approved:
        if instance.benefit:
            # Update
            Benefit.objects.filter(id=instance.benefit.id).update(**instance.contribution)
        else:
            # Create
            benefit = Benefit.objects.create(**instance.contribution)
            benefit.contribution_set.add(instance)

        if instance.email:
            check_promotion(Contribution.objects.filter(email=instance.email), instance.email)
