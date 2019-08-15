# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

"""
-------------------------------------------------
   File Name：     config
   Description :
   Author :       burt
   date：          2018-11-26
-------------------------------------------------
   Change Activity:
                   2018-11-26:
-------------------------------------------------
"""

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-xu_bo_bo'

    basedir = os.path.abspath(os.path.dirname(__file__))

    print(basedir)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # config admin email
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [os.environ.get('ADMINS_MAIL')]

    # log file
    LOG_FILE = 'logs/microblog.log'

    # paginate
    POSTS_PER_PAGE = 3

    # language for local
    LANGUAGES = ['en', 'es', 'zh_CN']

    # elastic search
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
