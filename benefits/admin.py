from django.contrib import admin
from .models import Benefit, Category, Contribution


class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'link')


admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Category)
admin.site.register(Contribution)
