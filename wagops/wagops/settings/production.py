from .base import *

STATIC_URL = "static/"
DEBUG = False
SECRET_KEY = "5m$x8nxvk$!3c9m^c!o8*a-*4fn#ox@ag2vb45$9sgrf25of)1"
ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://*.ondigitalocean.app"]
#SECURE_SSL_REDIRECT = True 
#SECURE_HSTS_SECONDS = 0

try:
    from .local import *
except ImportError:
    pass
