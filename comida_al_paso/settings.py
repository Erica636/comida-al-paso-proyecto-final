from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv

# Cargar variables de entorno desde .env si existe
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-this-in-production')

# Environment
ENV = os.getenv('ENV', 'development').lower()

# SECURITY WARNING: don't run with debug turned on in production!
# Acepta valores: "True", "true", "1", "yes"
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

# ALLOWED_HOSTS: lee la variable ALLOWED_HOSTS (coma separada) y limpia espacios
_raw_allowed = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0')
ALLOWED_HOSTS = [h.strip() for h in _raw_allowed.split(',') if h.strip()]

# Si se configuró RAILWAY_HOST (u otra variable) la agregamos automáticamente
# Útil si Railway te da la URL y la pones en esa variable
railway_host = os.getenv('RAILWAY_HOST') or os.getenv('RAILWAY_APP_HOST') or os.getenv('HOSTNAME')
if railway_host:
    railway_host = railway_host.strip()
    if railway_host and railway_host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(railway_host)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    
    # Local apps
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise para archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'comida_al_paso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'comida_al_paso.wsgi.application'

# Database - Detectar automáticamente si es MySQL o SQLite
DB_ENGINE = os.getenv('DB_ENGINE', 'django.db.backends.sqlite3')

if 'mysql' in DB_ENGINE.lower():
    # Configuración para MySQL (Railway)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQLDATABASE', 'railway'),
            'USER': os.getenv('MYSQLUSER', 'root'),
            'PASSWORD': os.getenv('MYSQLPASSWORD', ''),
            'HOST': os.getenv('MYSQLHOST', 'localhost'),
            'PORT': os.getenv('MYSQLPORT', '3306'),
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        }
    }
else:
    # Configuración para SQLite (desarrollo local)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDAT
