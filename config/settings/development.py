"""
Development settings for Takhlees Business project.
"""

from .base import *  # noqa: F403
import os

DEBUG = True

ALLOWED_HOSTS = list(ALLOWED_HOSTS) + ['testserver', 'localhost', '127.0.0.1']

# In development, support smooth local developer onboarding via SQLite
# when USE_SQLITE_DEV=True, or when PostgreSQL credentials are not yet configured.
if env.bool('USE_SQLITE_DEV', default=True) or env('DB_ENGINE', default='') == 'django.db.backends.sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
        }
    }

# Email backend for development (outputs to console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Relax password requirements in development for local testing
AUTH_PASSWORD_VALIDATORS = []
