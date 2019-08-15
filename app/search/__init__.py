# -*- coding: utf-8 -*-
from flask import Blueprint

"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       Administrator
   date：          2019/8/15 0015
-------------------------------------------------
   Change Activity:
                   2019/8/15 0015:
-------------------------------------------------
"""
bp = Blueprint('search', __name__)

from app.search import routes
