"""
The code in this module borrows heavily from https://github.com/dan-passaro/django-auto-repr/
which requires the MIT license to be included:

MIT License

Copyright (c) 2017 Daniel Passaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
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
            return f"{cls.__name__}(\n{app_config['MULTILINE_WHITESPACE']}{attrs},\n)"
        else:
            attrs = ', '.join(parts)
            return f'{cls.__name__}({attrs})'
