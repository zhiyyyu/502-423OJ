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

# JUDGE
LANGUAGE_SRC_FILE = {
    'C++': 'main.cpp',
    'C': 'main.c',
    'Java': 'Main.java',
    'Python3': 'main.py',
}
LANGUAGE_OUT_FILE = {
    'C++': 'main',
    'C': 'main',
    'Java': 'Main',
    'Python3': 'main',
}
BUILD_CMD = {
    "C": "gcc main.c -o main && ./main",
    "C++": "g++ main.cpp -o main && ./main",
    "Java": "javac Main.java",
    "Python3": 'python3 main.py',
    # "ruby": "ruby -c main.rb",
    # "perl": "perl -c main.pl",
    # "pascal": 'fpc main.pas -O2 -Co -Ct -Ci',
    # "go": '/opt/golang/bin/go build -ldflags "-s -w"  main.go',
    # "lua": 'luac -o main main.lua',
    # "python2": 'python2 -m py_compile main.py',
    # "haskell": "ghc -o main main.hs",
}