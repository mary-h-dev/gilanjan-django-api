from datetime import timedelta
import os
from pathlib import Path
from dotenv import load_dotenv
from corsheaders.defaults import default_headers, default_methods



BASE_DIR = Path(__file__).resolve().parent.parent
# env_path = r'C:\Users\novin\Desktop\safarman\safarman\safarman-backend\.env.dev'
# load_dotenv(env_path)




# SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY="django-insecure-lickuqb_5_dwg08)+_!ow40d5#v)(d6ht88ccn#z+s7+un2#3t"
WEBSITE_URL = 'https://api.gilanjan.com'
DEBUG = False
# ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1 [::1]").split(" ")
# print(f"SECRET_KEY: {SECRET_KEY}")
# print(f"DEBUG: {DEBUG}")
# print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")



ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '127.0.0.1',
    'gilanjan.com',
    'www.gilanjan.com',
    'api.gilanjan.com',
    'www.api.gilanjan.com',
]


CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'https://gilanjan.com',
    'http://gilanjan.com',
    'https://api.gilanjan.com',
    'http://api.gilanjan.com',
]

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'https://gilanjan.com',
    'http://gilanjan.com',
    'https://api.gilanjan.com',
    'http://api.gilanjan.com',
]







CORS_ALLOW_HEADERS = list(default_headers) + [
    "x-csrftoken",
]

CORS_ALLOW_METHODS = list(default_methods) + [
    "POKE",
]


CORS_ALLOW_ALL_ORIGINS = True


AUTH_USER_MODEL = 'useraccount.User'
SITE_ID = 1




# for websocket
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}



#for auth
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKEN": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "acomplexkey",
    "ALOGRIGTHM": "HS512",
}



ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = None



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    #     'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    
    # ),
}







REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False
}

# Application definition

INSTALLED_APPS = [
    'daphne',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",


    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    # 'django_filters',
    # 'drf_yasg',
    'django_ckeditor_5',
    

    'allauth',
    'allauth.account',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'corsheaders',

 
    'property',
    'useraccount',
    'chat',
    'tag',
    'blog',
    'food',
    'festival',
    'photos',
]



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "config.urls"



TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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



# WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = 'config.asgi.application'




# Database
#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
#    }
#}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  
        "NAME": os.environ.get("DB_NAME", "root"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "VTpjiIDgC23613wQHNm1ConP"),
        "HOST": os.environ.get("DB_HOST", "post-db"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}



CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading', '|',
                'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', '|',
                'undo', 'redo'
            ]
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', 'imageStyle:full', 'imageStyle:side'
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells'
            ]
        },
        'height': '300px',
        'width': '100%',
        'placeholder': 'Start typing here...',
    },
    'advanced': {
        'toolbar': {
            'items': [
                'heading', '|',
                'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', '|',
                'insertTable', 'uploadImage', '|',
                'undo', 'redo'
            ]
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', 'imageStyle:full', 'imageStyle:side'
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells'
            ]
        },
        'height': '400px',
        'width': '100%',
        'placeholder': 'Start typing here...',
        'extraPlugins': ['uploadimage'],  # اگر آپلود تصویر نیاز دارید
    },
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DJANGO_CKEDITOR_5_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
