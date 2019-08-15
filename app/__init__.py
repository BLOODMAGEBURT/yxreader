# -*- coding: utf-8 -*-
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from config import Config

"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       xubobo
   date：          2019/8/15 0015
-------------------------------------------------
   Change Activity:
                   2019/8/15 0015:
-------------------------------------------------
"""

# flask-login
login = LoginManager()
# login.login_view = 'auth.login'
# email
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    login.init_app(app)
    mail.init_app(app)
    # send error email
    if not (app.debug or app.testing):
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr=app.config['MAIL_USERNAME'],
                toaddrs=app.config['ADMINS'],
                subject='Microblog Failure',
                credentials=auth,
                secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        # log into the file
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            filename=app.config['LOG_FILE'],
            maxBytes=10240,
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: '
                                                    '%(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')

    return app
