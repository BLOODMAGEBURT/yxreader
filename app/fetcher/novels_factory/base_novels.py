#!/usr/bin/env python
"""
 Created by howie.hu at 2018/5/28.
"""
import logging

import requests
from requests import RequestException

from config import Config
from rules import BLACK_DOMAIN, RULES, LATEST_RULES

logging.basicConfig(level=logging.INFO)


class BaseNovels:
    """
    小说抓取父类
    """

    def __init__(self, logger=None):
        self.black_domain = BLACK_DOMAIN
        self.config = Config
        self.latest_rules = LATEST_RULES
        self.rules = RULES

    def fetch_url(self, url, params, headers):
        """
        公共抓取函数
        :param client:
        :param url:
        :param params:
        :param headers:
        :return:
        """
        try:
            res = requests.get(url, params=params, headers=headers)
            assert res.status_code == 200
            text = res.text
            return text
        except RequestException as e:
            logging.info(e)
            return None

    @classmethod
    def start(cls, novels_name):
        return cls().novels_search(novels_name)

    def data_extraction(self, html):
        """
        小说信息抓取函数
        :return:
        """
        raise NotImplementedError

    def novels_search(self, novels_name):
        """
        小说搜索入口函数
        :return:
        """
        raise NotImplementedError
