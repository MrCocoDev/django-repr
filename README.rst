.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/django-better-repr.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/django-better-repr
    .. image:: https://readthedocs.org/projects/django-better-repr/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://django-better-repr.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/django-better-repr/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/django-better-repr
    .. image:: https://img.shields.io/conda/vn/conda-forge/django-better-repr.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/django-better-repr
    .. image:: https://pepy.tech/badge/django-better-repr/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/django-better-repr
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/django-better-repr

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/
.. image:: https://img.shields.io/pypi/v/django-better-repr.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/django-better-repr/
.. image:: https://pepy.tech/badge/django-better-repr/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/django-better-repr

|

==================
django-better-repr
==================


    Django model reprs for humans!


This project seeks to make reprs of Django models more human-friendly. This
project is heavily inspired by https://github.com/dan-passaro/django-auto-repr .

Installation
============

::

   pip install django-better-repr

If you want to automatically improve the repr of all models in your project then add `django_better_repr`
to your installed apps.

::

   # settings.py
   INSTALLED_APPS = [
      ...,
      'django_better_repr',
      ...,
   ]

Want to customize which apps get configured but don't want to decorate each class individually?
Head on down to the **Configuration** section.

How to use:
===========

The repr logic in this library is designed to produce the smallest, most meaningful repr possible
for your Django models. That means that fields which aren't set won't show up in the repr. This
should reduce noise and let you get the most value out of your reprs.

::

   from django_better_repr import better_repr

   @better_repr
   class MyDjangoModel(models.Model):
       my_field = models.CharField(max_length=16)

Or, if class inheritance is more your speed:

::

   from django_better_repr.bases import BetterRepr

   class MyDjangoModel(BetterRepr, models.Model):
       my_field = models.CharField(max_length=16)

Then load up your favorite shell and run:

::

   MyDjangoModel.objects.create(my_field='Hello, world!')
   >>> MyDjangoModel(my_field='Hello, world!')

If your model has a lot of fields then the repr will automatically switch to
pretty printing. This can be configured via settings.

Configuration
=============

If you want to customize the behavior of the library, below are all the options.

::

   # settings.py
   BETTER_REPR_CONFIG = {
      'ENABLE_MULTILINE_REPRS': True,  # bool (default: True), whether or not to allow multiline reprs
      'SINGLE_LINE_PARTS_LIMIT': 4,  # int (default: 4), the number of fields a repr can have before switching to multi line
      'MULTILINE_WHITESPACE': '\t',  # str (default: '\t'), the whitespace string to use for multiline reprs
      'AUTO_CONFIGURE_INCLUDE_MODELS': [],  # list (default: a sentinel for all models), which models to auto include if the auto configuration application is added to INSTALLED_APPS
      'AUTO_CONFIGURE_EXCLUDE_MODELS': [],  # list (default: []), which models to exclude from the auto setup if the auto configuration application is added to INSTALLED_APPS
   }


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd django-better-repr
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate


.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
