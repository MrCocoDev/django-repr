from django.apps import apps

from django_better_repr import better_repr
from django_better_repr.config import ALL_APPS, app_config


def auto_configure():
    include = app_config['AUTO_CONFIGURE_INCLUDE_MODELS']
    if include is ALL_APPS:
        include = apps.get_models()

    exclude = {x for x in app_config['AUTO_CONFIGURE_EXCLUDE_MODELS']}
    models = {x for x in include}.difference(exclude)

    for model in models:
        better_repr()(model)
