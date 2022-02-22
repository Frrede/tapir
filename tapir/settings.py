"""
Django settings for tapir project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import sys
from pathlib import Path

import celery.schedules
import email.utils
import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "SECRET_KEY", default="fl%20e9dbkh4mosi5$i$!5&+f^ic5=7^92hrchl89x+)k0ctsn"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=list, default=["*"])

ENABLE_SILK_PROFILING = False

# Application definition
INSTALLED_APPS = [
    # Must come before contrib.auth to let the custom templates be discovered for auth views
    "tapir.accounts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_bootstrap5",
    "tapir.core",
    "tapir.log",
    "tapir.shifts",
    "tapir.utils",
    "tapir.coop",
    "tapir.odoo",
    "bootstrap_datepicker_plus",
    "django_tables2",
    "django_filters",
    "django_select2",  # For autocompletion in form fields
    "phonenumber_field",
    # TODO(Leon Handreke): Don't install in prod
    "django_extensions",
]

if ENABLE_SILK_PROFILING:
    INSTALLED_APPS.append("silk")


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "tapir.accounts.middleware.ClientPermsMiddleware",
    "tapir.accounts.models.language_middleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if ENABLE_SILK_PROFILING:
    MIDDLEWARE = ["silk.middleware.SilkyMiddleware"] + MIDDLEWARE

ROOT_URLCONF = "tapir.urls"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "tapir/templates")],
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

WSGI_APPLICATION = "tapir.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": env.db(default="postgresql://tapir:tapir@db:5432/tapir"),
    "ldap": env.db_url(
        "LDAP_URL", default="ldap://cn=admin,dc=supercoop,dc=de:admin@openldap"
    ),
}

DATABASE_ROUTERS = ["ldapdb.router.Router"]

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"
CELERY_BEAT_SCHEDULE = {
    "send_shift_reminders": {
        "task": "tapir.shifts.tasks.send_shift_reminders",
        "schedule": celery.schedules.crontab(
            hour="*/2", minute=5
        ),  # Every two hours five after the hour
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
PASSWORD_RESET_TIMEOUT = (
    7776000  # 90 days, so that the welcome emails stay valid for long enough
)


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "de"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# django-environ EMAIL_URL mechanism is a bit hairy with passwords with slashes in them, so use this instead
EMAIL_ENV = env("EMAIL_ENV", default="dev")
if EMAIL_ENV == "dev":
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
elif EMAIL_ENV == "test":
    # Local SMTP
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
elif EMAIL_ENV == "prod":
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp-relay.gmail.com"
    EMAIL_HOST_USER = "mitglied@supercoop.de"
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

EMAIL_ADDRESS_MEMBER_OFFICE = "mitglied@supercoop.de"
FROM_EMAIL_MEMBER_OFFICE = f"SuperCoop Mitgliederbüro <{EMAIL_ADDRESS_MEMBER_OFFICE}>"
DEFAULT_FROM_EMAIL = FROM_EMAIL_MEMBER_OFFICE


# DJANGO_ADMINS="Blake <blake@cyb.org>, Alice Judge <alice@cyb.org>"
ADMINS = tuple(email.utils.parseaddr(x) for x in env.list("DJANGO_ADMINS", default=[]))
# Crash emails will come from this address.
# NOTE(Leon Handreke): I don't know if our Google SMTP will reject other senders, so play it safe.
SERVER_EMAIL = "mitglied@supercoop.de"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "tapir/static")]
STATIC_ROOT = os.path.join(BASE_DIR, "core/static")

SELECT2_JS = "select2/4.0.13/js/select2.min.js"
SELECT2_CSS = "select2/4.0.13/css/select2.min.css"
SELECT2_I18N_PATH = "select2/4.0.13/js/i18n"

WEASYPRINT_BASEURL = "/"

REG_PERSON_BASE_DN = "ou=people,dc=supercoop,dc=de"
REG_PERSON_OBJECT_CLASSES = ["inetOrgPerson", "organizationalPerson", "person"]
REG_GROUP_BASE_DN = "ou=groups,dc=supercoop,dc=de"
REG_GROUP_OBJECT_CLASSES = ["groupOfNames"]

# Groups are stored in the LDAP tree
GROUP_VORSTAND = "vorstand"
GROUP_MEMBER_OFFICE = "member-office"
# This is our own little stupid permission system. See explanation in accounts/models.py.
PERMISSIONS = {
    "shifts.manage": [GROUP_VORSTAND, GROUP_MEMBER_OFFICE],
    "coop.view": [GROUP_VORSTAND, GROUP_MEMBER_OFFICE],
    "coop.manage": [GROUP_VORSTAND, GROUP_MEMBER_OFFICE],
    # TODO(Leon Handreke): Reserve this to a list of knowledgeable superusers
    "coop.admin": [GROUP_VORSTAND, GROUP_MEMBER_OFFICE],
    "accounts.view": [GROUP_VORSTAND, GROUP_MEMBER_OFFICE],
    "accounts.manage": [GROUP_VORSTAND, GROUP_MEMBER_OFFICE],
    "welcomedesk.view": [GROUP_VORSTAND, GROUP_MEMBER_OFFICE],
}

# Permissions granted to client presenting a given SSL client cert. Currently used for the welcome desk machines.
CLIENT_PERMISSIONS = {
    "CN=welcome-desk.members.supercoop.de,O=SuperCoop Berlin eG,C=DE": [
        "welcomedesk.view",
    ]
}

AUTH_USER_MODEL = "accounts.TapirUser"
LOGIN_REDIRECT_URL = "accounts:user_me"

SITE_URL = env("SITE_URL", default="http://127.0.0.1:8000")

PHONENUMBER_DEFAULT_REGION = "DE"

LOCALE_PATHS = [os.path.join(BASE_DIR, "tapir/translations/locale")]

if ENABLE_SILK_PROFILING:
    SILKY_PYTHON_PROFILER = True
    SILKY_PYTHON_PROFILER_BINARY = True
    SILKY_META = True
