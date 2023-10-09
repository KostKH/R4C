import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    default='mztx@x_-=gfhc9xs@bm58m&@3pc7##opo14zob!(l2tus05+jo'
)
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'robots.apps.RobotsConfig',
    'customers.apps.CustomersConfig',
    'orders.apps.OrdersConfig',
    'reporting.apps.ReportingConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'R4C.urls'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
INCLUDES = os.path.join(TEMPLATES_DIR, 'reporting/includes')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, INCLUDES],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'R4C.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

ORDER_MODEL = 'orders.Order'
ROBOT_MODEL = 'robots.Robot'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

RABBITMQ = {
    'PROTOCOL': 'amqp',
    'HOST': os.getenv('RABBITMQ_HOST', 'localhost'),
    'PORT': os.getenv('RABBITMQ_PORT', 5672),
    'USER': os.getenv('RABBITMQ_DEFAULT_USER', 'guest'),
    'PASSWORD': os.getenv('RABBITMQ_DEFAULT_PASS', 'guest'),
}
CELERY_BROKER_URL = (f'{RABBITMQ["PROTOCOL"]}://{RABBITMQ["USER"]}:'
                     f'{RABBITMQ["PASSWORD"]}@{RABBITMQ["HOST"]}:'
                     f'{RABBITMQ["PORT"]}')
