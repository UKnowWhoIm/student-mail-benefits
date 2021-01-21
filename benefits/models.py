from django.db import models


def check_promotion(email, count):
    # TODO check for
    pass


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Benefit(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, related_name="benefits", on_delete=models.SET_NULL, null=True)
    highlights = models.JSONField(default=list)
    link = models.CharField(max_length=100)
    img_file = models.CharField(max_length=2048, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contribution(models.Model):
    email = models.EmailField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    contribution = models.JSONField()
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.approved:
            benefit = Benefit.objects.get(id=self.benefit.id)
            if self.contribution:
                # Update
                benefit.update(**self.contribution)
            else:
                # Create
                benefit.update(is_verified=True)

            if self.email:
                check_promotion(len(Contribution.objects.filter(email=self.email, approved=True)), self.email)

        super().save(force_insert, force_update, using, update_fields)
