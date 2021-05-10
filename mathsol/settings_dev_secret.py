# This is a template file for developer specific options
# Copy this file to `settings_dev_secret.py`
# DO NOT commit this file to GIT


from . import settings


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'db.sqlite3',
    }
}
