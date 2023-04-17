.. _installation:


Installation
============

The django-hostutils package is available on Python Package Index (PyPI) and can be installed via pip with the
following command:

.. code-block:: console

    pip install django-hostutils
..


To use django-hostutils in your project, add 'djangoaddicts.hostutils' to INSTALLED_APPS in your settings.py file.

.. code-block:: python

    INSTALLED_APPS = [
        ...
       'djangoaddicts.hostutils',
    ]
..


Several views, with applicable Bootstrap 5 templates, are provided for use. To user these, include the hostutils urls in your project-level urs.py file.

.. code-block:: python

    urlpatterns = [
        ...
        path("hostutils/", include("djangoaddicts.hostutils.urls"), ),
    ]
..

|
