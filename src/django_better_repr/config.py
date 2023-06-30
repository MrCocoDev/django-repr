from unittest.mock import sentinel

from django.conf import settings

ALL_APPS = sentinel.ALL_APPS

settings_attr = getattr(settings, 'BETTER_REPR_CONFIG', {})

app_config = {
    'SINGLE_LINE_PARTS_LIMIT': settings_attr.get('SINGLE_LINE_PARTS_LIMIT', 4),
    'ENABLE_MULTILINE_REPRS': settings_attr.get('ENABLE_MULTILINE_REPRS', True),
    'MULTILINE_WHITESPACE': settings_attr.get('MULTILINE_WHITESPACE', '\t'),
    'AUTO_CONFIGURE_INCLUDE_MODELS': settings_attr.get('AUTO_CONFIGURE_INCLUDE_MODELS', ALL_APPS),
    'AUTO_CONFIGURE_EXCLUDE_MODELS': settings_attr.get('AUTO_CONFIGURE_EXCLUDE_MODELS', []),
}
