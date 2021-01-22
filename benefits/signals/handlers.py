from django.db.models.signals import post_save
from django.dispatch import receiver
from benefits.models import Contribution, Benefit, Category
from benefits.utils import check_promotion


@receiver(post_save, sender=Contribution)
def make_contribution(sender, instance, created, **kwargs):
    if instance.approved:
        contribution = instance.contribution
        if contribution.get("category"):
            contribution["category"] = Category.objects.get(id=contribution["category"])
        if instance.benefit:
            # Update
            benefit = Benefit.objects.get(id=instance.benefit.id).update(**contribution)
        else:
            # Create
            benefit = Benefit.objects.create(**contribution)
            benefit.contribution_set.add(instance)

        benefit.save()

        if instance.email:
            check_promotion(Contribution.objects.filter(email=instance.email), instance.email)
