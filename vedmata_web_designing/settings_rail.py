from vedmata_web_designing.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')

CSRF_TRUSTED_ORIGINS = [
    'https://vmdonline.in',
]
