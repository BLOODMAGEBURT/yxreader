#!/usr/bin/env python
"""
 Created by howie.hu at 2018/5/28.
"""

import logging
import os
import random
import time
from urllib.parse import urlparse

import cchardet
import requests
from requests import RequestException

from config import Config

logging.basicConfig(level=logging.INFO)


def _get_data(filename, default='') -> list:
    """
    Get data from a file
    :param filename: filename
    :param default: default value
    :return: data
    """
    root_folder = os.path.dirname(os.path.dirname(__file__))
    user_agents_file = os.path.join(
        os.path.join(root_folder, 'data'), filename)
    try:
        with open(user_agents_file, 'r') as f:
            data = [_.strip() for _ in f.readlines()]
    except:
        data = [default]
    return data


def get_random_user_agent() -> str:
    """
    Get a random user agent string.
    :return: Random user agent string.
    """
    return random.choice(_get_data('user_agents.txt', Config.USER_AGENT))


def get_time() -> str:
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return time_str


def get_netloc(url):
    """
    获取netloc
    :param url: 
    :return:  netloc
    """
    netloc = urlparse(url).netloc
    return netloc or None


def target_fetch(url, headers, timeout=15):
    """
    :param url: target url
    :return: text
    """
    try:
        res = requests.get(url, headers=headers)
        assert res.status_code == 200
        logging.info('Task url: {}'.format(res.url))

        text = res.text
    except RequestException as e:
        logging.exception(e)
        text = None

    return text


def get_html_by_requests(url, headers, timeout=15):
    """
    :param url:
    :return:
    """
    try:
        response = requests.get(url=url, headers=headers, verify=False, timeout=timeout)
        response.raise_for_status()
        content = response.content
        charset = cchardet.detect(content)
        text = content.decode(charset['encoding'])
        return text
    except Exception as e:
        logging.exception(e)
        return None
