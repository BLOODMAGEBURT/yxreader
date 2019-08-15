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

    # yxreader
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    TIMEZONE = 'Asia/Shanghai'

    # Engine config
    URL_PHONE = 'https://m.baidu.com/s'
    URL_PC = 'http://www.baidu.com/s'
    BAIDU_RN = 15
    SO_URL = "https://www.so.com/s"
    BY_URL = "https://www.bing.com/search"
    DUCKGO_URL = "https://duckduckgo.com/html"
