import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'ngu!*gtkqd!unon5t#y_7u=^t!#5et46=&@a&(q^w5_*lx9vyj0l83002'

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['database.ngu.ua', 'demo-database.ngu.ua', '192.168.83.67', '127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'nguhub.sqlite3'),
    }
}


# email settings
# please, set here you smtp server details and your admin email
ADMIN_EMAIL = 'admin@ngu.ua'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = '***********'
EMAIL_HOST_PASSWORD = '********'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


 # admins
ADMINS = (('Ruslan', 'djrexxx87@gmail.comment'),)
MANAGERS = (('Ruslan', 'djrexx87@gmail.com'),)


DEFAULT_SITE_NAMING = 'в/ч 3002 м.Львів'