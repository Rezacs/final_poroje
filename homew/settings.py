"""
Django settings for homew project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*rf*grz$bx@9!*2(swzi^r*3xh+2cr=d76rc$(7nqb$z=mea_z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['bi3z.com' , 'www.bi3z.com']


# Application definition

INSTALLED_APPS = [
    'custom_login',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'drf_yasg',
    'widget_tweaks',
    'crispy_forms',

    'basket',
    'commentandlike',
    'customer',
    'grups',
    'products',
    'post',
    'articles',
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

ROOT_URLCONF = 'homew.urls'

# import os
# SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
#os.path.join(SETTINGS_PATH, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # injjjja
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.views.base_template',
            ],
        },
    },
]

WSGI_APPLICATION = 'homew.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myproject',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

LOGIN_URL = '/post_urls/login'
SWAGGER_SETTINGS = {
    'SHOW_REQUEST_HEADERS': True,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': True,
    'JSON_EDITOR': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
}
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#     'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ] ,
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# } 

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
} 




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS  = [
    # str(BASE_DIR)  +"/static",
    BASE_DIR / 'static' ,
]

MEDIA_ROOT =  str(BASE_DIR /'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GRAPH_MODELS = {
    "all_applications" : True ,
    "group_models" : True ,
}

LOCALE_PATHS = [
     str(BASE_DIR /'locale')
]

# REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

# 'DEFAULT_AUTHENTICATION_CLASSES': (
#     'rest_framework_simplejwt.authentication.JWTAuthentication',
# ) ,


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'atccereza@gmail.com'
EMAIL_HOST_PASSWORD = 'bakMAN12'

SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
}

# REST_FRAMEWORK = {
    
# }

AUTH_USER_MODEL = 'custom_login.MyUser'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'custom_login.mybackend.ModelBackend',
    'custom_login.mybackend.OtpBackend'
]
Kavenegar_API = '5A32762F6B374C2F7567504756465968595635662B51594D4E526D78494A31323573376735756A305032553D'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# LOGGING ={
#     'version':1,
#     #'disable_existing_loggers': True ,
#     'loggers':{
#         'django':{
#             'level':'DEBUG',
#             'handlers':['file','file2']
#         }
#     },
#     'handlers':{
#         'file':{
#             'level':'INFO',
#             'class':'logging.FileHandler',
#             'filename':'./logs/debug5.log',
#             'formatter':'simpleRe',
#         },
#         'file2':{
#             'level':'ERROR',
#             'class':'logging.FileHandler',
#             'filename':'./logs/error.log',
#             'formatter':'errorFormat',
#         }
#     },
#     'formatters':{
#         'simpleRe':{
#             'format':'{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style':'{',   # ya { ya $ ya #
#         },
#         'errorFormat':{
#             'format':'{asctime} {message}',
#             'style':'{',
#         }
#     }
# }

# django commands !
# django signals !
# django site map !


############



# """
# Django settings for homew project.

# Generated by 'django-admin startproject' using Django 3.2.9.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.2/ref/settings/
# """

# from pathlib import Path
# from datetime import timedelta

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-*rf*grz$bx@9!*2(swzi^r*3xh+2cr=d76rc$(7nqb$z=mea_z'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['bi3z.com' , 'www.bi3z.com']


# # Application definition

# INSTALLED_APPS = [
#     'custom_login',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django_extensions',
#     'rest_framework',
#     'django_filters',
#     'rest_framework_simplejwt',
#     'drf_yasg',
#     'widget_tweaks',
#     'crispy_forms',

#     'basket',
#     'commentandlike',
#     'customer',
#     'grups',
#     'products',
#     'post',
#     'articles',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'homew.urls'

# import os
# # SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
# #os.path.join(SETTINGS_PATH, 'templates')

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [], # injjjja
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'products.views.base_template',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'homew.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# #         'NAME': 'myproject',
# #         'USER': 'myprojectuser',
# #         'PASSWORD': 'password',
# #         'HOST': 'localhost',
# #         'PORT': '',
# #     }
# # }

# LOGIN_URL = '/post_urls/login'
# SWAGGER_SETTINGS = {
#     'SHOW_REQUEST_HEADERS': True,
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header'
#         }
#     },
#     'USE_SESSION_AUTH': True,
#     'JSON_EDITOR': True,
#     'SUPPORTED_SUBMIT_METHODS': [
#         'get',
#         'post',
#         'put',
#         'delete',
#         'patch'
#     ],
# }
# # REST_FRAMEWORK = {
# #     'DEFAULT_AUTHENTICATION_CLASSES': [
# #     'rest_framework_simplejwt.authentication.JWTAuthentication',
# #     ] ,
# #     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# # } 

# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# } 




# # Password validation
# # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Tehran'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = False


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# # STATICFILES_DIRS  = [
# #     # str(BASE_DIR)  +"/static",
# #     BASE_DIR / 'static' ,
# # ]

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# MEDIA_ROOT =  str(BASE_DIR /'media')
# MEDIA_URL = '/media/'

# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# GRAPH_MODELS = {
#     "all_applications" : True ,
#     "group_models" : True ,
# }

# LOCALE_PATHS = [
#      str(BASE_DIR /'locale')
# ]

# # REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

# # 'DEFAULT_AUTHENTICATION_CLASSES': (
# #     'rest_framework_simplejwt.authentication.JWTAuthentication',
# # ) ,


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'atccereza@gmail.com'
# EMAIL_HOST_PASSWORD = 'bakMANsUper@11228'

# SIMPLE_JWT = {
# 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
# }

# # REST_FRAMEWORK = {
    
# # }

# AUTH_USER_MODEL = 'custom_login.MyUser'


# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'custom_login.mybackend.ModelBackend',
#     'custom_login.mybackend.OtpBackend'
# ]
# Kavenegar_API = '5A32762F6B374C2F7567504756465968595635662B51594D4E526D78494A31323573376735756A305032553D'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'

# # LOGGING ={
# #     'version':1,
# #     #'disable_existing_loggers': True ,
# #     'loggers':{
# #         'django':{
# #             'level':'DEBUG',
# #             'handlers':['file','file2']
# #         }
# #     },
# #     'handlers':{
# #         'file':{
# #             'level':'INFO',
# #             'class':'logging.FileHandler',
# #             'filename':'./logs/debug5.log',
# #             'formatter':'simpleRe',
# #         },
# #         'file2':{
# #             'level':'ERROR',
# #             'class':'logging.FileHandler',
# #             'filename':'./logs/error.log',
# #             'formatter':'errorFormat',
# #         }
# #     },
# #     'formatters':{
# #         'simpleRe':{
# #             'format':'{levelname} {asctime} {module} {process:d} {thread:d} {message}',
# #             'style':'{',   # ya { ya $ ya #
# #         },
# #         'errorFormat':{
# #             'format':'{asctime} {message}',
# #             'style':'{',
# #         }
# #     }
# # }

# # django commands !
# # django signals !
# # django site map !