from django.contrib import admin
from .models import Benefit, Category


class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'link', 'is_verified')


admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Category)
