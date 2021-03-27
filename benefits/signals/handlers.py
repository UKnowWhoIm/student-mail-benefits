from django.db.models.signals import post_save
from django.dispatch import receiver
from benefits.models import Contribution, Benefit, Category
from users.utils import check_promotion


@receiver(post_save, sender=Contribution)
def make_contribution(sender, instance, created, **kwargs):
    if instance.approved:

        contribution = instance.contribution
        if contribution.get("category"):
            contribution["category"] = Category.objects.get(id=contribution["category"])

        if instance.benefit:
            # Update
            Benefit.objects.filter(id=instance.benefit.id).update(**instance.contribution)
        else:
            # Create
            benefit = Benefit.objects.create(**instance.contribution)
            benefit.contribution_set.add(instance)

        if instance.email:
            check_promotion(len(Contribution.objects.filter(email=instance.email, approved=True)), instance.email)
