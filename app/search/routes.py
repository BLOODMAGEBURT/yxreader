# -*- coding: utf-8 -*-
import logging
import time
from operator import itemgetter

from flask import render_template, request, redirect

from app.fetcher.cache import cache_owllook_novels_chapter
from app.fetcher.function import get_netloc
from app.fetcher.novels_tools import get_novels_info
from app.search import bp
from rules import RULES, REPLACE_RULES

logging.basicConfig(level=logging.INFO)
"""
-------------------------------------------------
   File Name：     routes
   Description :
   Author :       Administrator
   date：          2019/8/15 0015
-------------------------------------------------
   Change Activity:
                   2019/8/15 0015:
-------------------------------------------------
"""


@bp.route('/')
def index():
    return render_template('index.html', title='yxreader - 网络小说阅读', is_login=0)


@bp.route('/search', methods=['GET'])
def search():
    start = time.time()
    name = request.args.get('wd').strip()
    novels_keyword = name.split(' ')[0]
    if not name:
        return redirect('/')

    # 通过搜索引擎获取检索结果
    novels_name = 'intitle:{name} 小说 阅读'.format(name=name)
    parse_result = get_novels_info(class_name='baidu', novels_name=novels_name)
    parse_result = [x for x in parse_result if x is not None]
    logging.info(parse_result)
    if parse_result:
        # 优先依靠是否解析进行排序  其次以更新时间进行排序
        result_sorted = sorted(
            parse_result,
            reverse=True,
            key=itemgetter('is_recommend', 'is_parse', 'timestamp'))

        return render_template(
            'result.html',
            is_login=0,
            name=novels_keyword,
            time='{:.2f}'.format(time.time() - start),
            result=result_sorted,
            count=len(parse_result))


@bp.route('/chapter', methods=['GET'])
def chapter():
    """
        返回小说章节目录页
        : content_url   这决定当前U页面url的生成方式
        : url           章节目录页源url
        : novels_name   小说名称
        :return: 小说章节内容页
        """
    url = request.args.get('url', None)
    novels_name = request.args.get('novels_name', None)
    netloc = get_netloc(url)
    if netloc not in RULES.keys():
        return redirect(url)
    if netloc in REPLACE_RULES.keys():
        url = url.replace(REPLACE_RULES[netloc]['old'], REPLACE_RULES[netloc]['new'])
    content_url = RULES[netloc].content_url
    content = await cache_owllook_novels_chapter(url=url, netloc=netloc)
    if content:
        content = str(content).strip('[],, Jjs').replace(', ', '').replace('onerror', '').replace('js', '').replace(
            '加入书架', '')
        return render_template(
            'chapter.html', novels_name=novels_name, url=url, content_url=content_url, soup=content)
    else:
        return '解析失败，请将失败页面反馈给本站，请重新刷新一次，或者访问源网页：{url}'.format(url=url)
