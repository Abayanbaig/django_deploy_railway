from mysite.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')


ALLOWED_HOSTS = ['web-production-f709.up.railway.app']