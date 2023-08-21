from functools import lru_cache
from unittest.mock import sentinel

from django.conf import settings

ALL_APPS = sentinel.ALL_APPS


@lru_cache(maxsize=1)
def config():
    settings_attr = getattr(settings, 'BETTER_REPR_CONFIG', {})

    return {
        # Which models to automatically to include
        'AUTO_CONFIGURE_INCLUDE_MODELS': settings_attr.get('AUTO_CONFIGURE_INCLUDE_MODELS', ALL_APPS),
        # Which models to exclude from automatic inclusion
        'AUTO_CONFIGURE_EXCLUDE_MODELS': settings_attr.get('AUTO_CONFIGURE_EXCLUDE_MODELS', []),
        # Enable multiline REPRs
        'ENABLE_MULTILINE_REPRS': settings_attr.get('ENABLE_MULTILINE_REPRS', True),
        # Should deferred fields be included (1 query per deferred field)
        'EXCLUDE_DEFERRED_FIELDS': settings_attr.get('EXCLUDE_DEFERRED_FIELDS', True),
        # What whitespace to use for multiline REPRs, this is so we don't need to debate spaces vs tabs
        'MULTILINE_WHITESPACE': settings_attr.get('MULTILINE_WHITESPACE', '\t'),
        # How many parts (example: id=1) before splitting into a new line
        'SINGLE_LINE_PARTS_LIMIT': settings_attr.get('SINGLE_LINE_PARTS_LIMIT', 4),
    }
