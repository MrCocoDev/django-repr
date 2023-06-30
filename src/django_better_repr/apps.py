from django.apps import AppConfig

from django_better_repr.signals import auto_configure


class DjangoBetterReprAutoConfigure(AppConfig):
    default = True
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_better_repr'

    def ready(self):
        auto_configure()
