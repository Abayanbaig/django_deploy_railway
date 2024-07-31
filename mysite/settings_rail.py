from mysite.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db.sqlite3',
#         'USER': 'postgres',
#         'PASSWORD': 'HrjdHQLUPhXNkIfWcMofRPjMdGZyitvB',
#         'HOST': 'postgres.railway.internal.railway.app',  # The hostname provided by Railway
#         'PORT': '5432',
#         'options':{'sslmode' : 'require' },
#     }
# }

ALLOWED_HOSTS = ['web-production-f709.up.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST':config('DATABASE_HOST'),  # The hostname provided by Railway
        'PORT': config('DATABASE_PORT'),
        'options':{'sslmode' : 'require' },
    }
}