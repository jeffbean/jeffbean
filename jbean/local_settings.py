# coding=utf-8
__author__ = 'jbean'
DEBUG = True

SECRET_KEY = ')g8k%z-(vv304(0ir#wf2vo+vt$c2yp^4$hd%^iz(2@i#lx*)('

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/dev.db',
        'ATOMIC_REQUESTS': True,
    }
}