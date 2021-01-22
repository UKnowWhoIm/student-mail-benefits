from django.apps import AppConfig


class BenefitsConfig(AppConfig):
    name = 'benefits'

    def ready(self):
        import benefits.signals.handlers