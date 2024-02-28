"""
Minimal file so Sphinx can work with Django for autodocumenting.

Location: /docs/django_settings.py
"""

from pathlib import Path

import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "test"

# INSTALLED_APPS with these apps is necessary for Sphinx to build
# without warnings & errors
# Depending on your package, the list of apps may be different
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "handyhelpers",
    "djangoaddicts.hostutils",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "tests.core.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        "TEST_NAME": "test.sqlite3",
        "USER": "hostutils",
        "PASSWORD": "hostutils",
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "core", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

BASE_TEMPLATE = "handyhelpers/handyhelpers_bs5/base.htm"

USE_TZ = True

MESSAGE_ON_PERMISSION_DENY = True

print(BASE_DIR)
