from os import environ

# databse
DATABASE_SETTING = {
    'DATABASE_NAME': "oj_db",
    'DATABASE_USER': environ.get('OJ_DATABASE_USER'),
    'DATABASE_PWD': environ.get('OJ_DATABASE_PWD'),
    'DATABASE_HOST': "localhost",
    'DATABASE_PORT': "3306",
}

# email
EMAIL_SETTING = {
    'EMAIL_HOST': environ.get('OJ_EMAIL_HOST'),
    'EMAIL_PORT': environ.get('OJ_EMAIL_PORT'),
    'EMAIL_HOST_USER': environ.get('OJ_EMAIL_HOST_USER'),
    'EMAIL_HOST_PASSWORD': environ.get('OJ_EMAIL_HOST_PASSWORD'),
    'EMAIL_FROM': environ.get('OJ_EMAIL_FROM')
}

# avatar
AVATAR_URI_PREFIX = ''
AVATAR_MAX_SIZE = 6 * 1024 * 1024
AVATAR_FILE_PATH = ''
AVATAR_SUPPORT_TYPE = ['.png', '.jpg', '.jpeg']

# JUDGE TOKEN
JUDGE_TOKEN = ''

JUDGE_URL = ''