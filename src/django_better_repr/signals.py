from django.apps import apps
from django.core.signals import setting_changed
from django.dispatch import receiver

from django_better_repr import better_repr
from django_better_repr.config import ALL_APPS, config


def auto_configure():
    include = config()['AUTO_CONFIGURE_INCLUDE_MODELS']
    if include is ALL_APPS:
        include = apps.get_models()

    exclude = {x for x in config()['AUTO_CONFIGURE_EXCLUDE_MODELS']}
    models = {x for x in include}.difference(exclude)

    for model in models:
        better_repr()(model)


@receiver(setting_changed)
def settings_changed_callback(sender, setting, value, enter, **kwargs):
    if setting == 'BETTER_REPR_CONFIG':
        config.cache_clear()
