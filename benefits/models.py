from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Benefit(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, related_name="benefits", on_delete=models.SET_NULL, null=True)
    link = models.CharField(max_length=100)
