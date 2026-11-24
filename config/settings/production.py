"""
Production settings for Takhlees Business project.
"""

from .base import *  # noqa: F403

DEBUG = False

# Security verification
if SECRET_KEY == 'insecure-default-key-for-building-must-override':  # noqa: F405
    raise ValueError("Production SECRET_KEY must be securely defined in environment variables!")

# HTTPS / SSL Security
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)  # noqa: F405
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=31536000)  # 1 year  # noqa: F405
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cloud Object Storage (AWS S3 or compatible)
if USE_S3_STORAGE:  # noqa: F405
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "access_key": env('AWS_ACCESS_KEY_ID'),  # noqa: F405
                "secret_key": env('AWS_SECRET_ACCESS_KEY'),  # noqa: F405
                "bucket_name": env('AWS_STORAGE_BUCKET_NAME'),  # noqa: F405
                "region_name": env('AWS_S3_REGION_NAME', default='me-central-1'),  # noqa: F405
                "default_acl": 'private',
                "file_overwrite": False,
                "querystring_auth": True,
            },
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

# Production Email (SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='smtp.sendgrid.net')  # noqa: F405
EMAIL_PORT = env.int('EMAIL_PORT', default=587)  # noqa: F405
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')  # noqa: F405
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')  # noqa: F405
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='noreply@takhleesbusiness.com')  # noqa: F405
