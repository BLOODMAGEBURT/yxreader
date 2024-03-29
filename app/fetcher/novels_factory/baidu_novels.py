#!/usr/bin/env python
"""
 Created by howie.hu at 2018/5/28.
"""

import logging
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from requests import RequestException

from app.fetcher.function import get_random_user_agent
from app.fetcher.novels_factory.base_novels import BaseNovels

logging.basicConfig(level=logging.INFO)


class BaiduNovels(BaseNovels):

    def __init__(self):
        super(BaiduNovels, self).__init__()

    def data_extraction(self, html):
        """
        小说信息抓取函数
        :return:
        """
        try:
            url = html.select('h3.t a')[0].get('href', None)
            real_url = self.get_real_url(url=url) if url else None
            if real_url:
                real_str_url = str(real_url)
                netloc = urlparse(real_str_url).netloc
                if "http://" + netloc + "/" == real_str_url:
                    return None
                if 'baidu' in real_str_url or netloc in self.black_domain:
                    return None
                is_parse = 1 if netloc in self.rules.keys() else 0
                title = html.select('h3.t a')[0].get_text()
                is_recommend = 1 if netloc in self.latest_rules.keys() else 0
                timestamp = 0
                time = ""
                return {'title': title, 'url': real_str_url.replace('index.html', ''), 'time': time,
                        'is_parse': is_parse,
                        'is_recommend': is_recommend,
                        'timestamp': timestamp,
                        'netloc': netloc}
            else:
                return None
        except Exception as e:
            logging.exception(e)
            return None

    def get_real_url(self, url):
        """
        获取百度搜索结果真实url
        :param url:
        :return:
        """
        try:
            headers = {'user-agent': get_random_user_agent()}
            res = requests.head(url, headers=headers, allow_redirects=True)
            logging.info('Parse url: {}'.format(res.url))
            url = res.url if res.url else None
            return url

        except RequestException as e:
            logging.exception(e)
        return None

    def novels_search(self, novels_name):
        """
        小说搜索入口函数
        :return:
        """
        url = self.config.URL_PC
        params = {'wd': novels_name, 'ie': 'utf-8', 'rn': self.config.BAIDU_RN, 'vf_bl': 1}
        headers = {'user-agent': get_random_user_agent()}
        html = self.fetch_url(url=url, params=params, headers=headers)
        if html:
            soup = BeautifulSoup(html, 'html5lib')
            result = soup.find_all(class_='result')
            extra_tasks = [self.data_extraction(html=i) for i in result]
            return extra_tasks
        else:
            return []


def start1(novels_name):
    """
    Start spider
    :return:
    """
    return BaiduNovels.start(novels_name)


if __name__ == '__main__':
    pass
    # Start
    # import aiocache
    #
    # REDIS_DICT = {}
    # aiocache.settings.set_defaults(
    #     class_="aiocache.RedisCache",
    #     endpoint=REDIS_DICT.get('REDIS_ENDPOINT', 'localhost'),
    #     port=REDIS_DICT.get('REDIS_PORT', 6379),
    #     db=REDIS_DICT.get('CACHE_DB', 0),
    #     password=REDIS_DICT.get('REDIS_PASSWORD', None),
    # )
    # res = asyncio.get_event_loop().run_until_complete(start('intitle:雪中悍刀行 小说 阅读'))
    # print(res)
