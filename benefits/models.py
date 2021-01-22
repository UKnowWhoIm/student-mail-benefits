from django.db import models


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

    @property
    def contributors(self):
        return [i.email for i in self.contribution_set.all() if i.email]

    def __str__(self):
        return self.title


class Contribution(models.Model):
    email = models.EmailField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    contribution = models.JSONField()
    benefit = models.ForeignKey(Benefit, on_delete=models.SET_NULL, null=True, rel="contributions", blank=True)
    approved = models.BooleanField(default=False)
