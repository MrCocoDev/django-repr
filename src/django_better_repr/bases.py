from functools import partial

from django.db import models

from django_better_repr.config import app_config
from django_better_repr.exceptions import BetterReprException


def _repr_format_field(self, field):
    if isinstance(field, models.ManyToManyField):
        return

    if isinstance(field, models.ForeignKey):
        field_name = field.name + '_id'
    else:
        field_name = field.name

    field_value = getattr(self, field_name)

    default = field.default
    if field_value == default:
        return ''
    elif default is models.NOT_PROVIDED:
        if isinstance(field, models.CharField) and field_value == '':
            return ''
        if field_value is None:
            return ''
    return f"{field_name}={repr(field_value)}"


class BetterRepr:
    def __repr__(self):
        cls = type(self)
        try:
            fields = cls._meta.fields
        except AttributeError as e:
            raise BetterReprException(f"{cls} does not appear to be a django model!") from e

        parts = list(filter(None, map(partial(_repr_format_field, self), fields)))
        if len(parts) > app_config['SINGLE_LINE_PARTS_LIMIT'] and app_config['ENABLE_MULTILINE_REPRS']:
            attrs = ',\n\t'.join(parts)
            return f"{cls.__name__}(\n\t{attrs},\n)"
        else:
            attrs = ', '.join(parts)
            return f'{cls.__name__}({attrs})'
