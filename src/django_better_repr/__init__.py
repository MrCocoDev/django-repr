import sys

from django_better_repr.bases import BetterRepr

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "django-better-repr"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


def better_repr(klass: type = None, /, ):
    def decorator(kls: type):
        if BetterRepr not in kls.__bases__:
            kls.__bases__ = (BetterRepr, *kls.__bases__)
        return kls

    if klass:
        return decorator(klass)
    else:
        return decorator
