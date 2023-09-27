# -*- coding: utf-8 -*-
# @Time    : 2023/9/27 14:41
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 爬虫工具类.py
# @Software: PyCharm
import json

from decorator import decorator
from requests_html import HTMLSession
from retrying import retry
from sympy.strategies import glom


class MetaSingleton(type):
    """ MetaSingleton """
    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._inst[cls]


class GetProxies(metaclass=MetaSingleton):
    """ GetProxies """
    ip = None

    def getproxy(self, change_proxy):
        """ GetProxy """
        if self.ip is None:
            self.ip = self.get_ip(HTMLSession())
            self.proxies = {
                'http': self.ip,
                'https': self.ip
            }
        if change_proxy:
            self.ip = self.get_ip(HTMLSession())
            self.proxies = {
                'http': self.ip,
                'https': self.ip
            }
        return self.proxies

    def get_ip(self, session):
        """get_ip"""
        url = 'ip'
        req = session.get(url)
        if req.status_code == 200:
            jsonstr = req.json()
            isok = glom(jsonstr, "resCode")
            if isok == "0000":
                key = glom(jsonstr, ('reData', ['key']))[0]
                uname = glom(jsonstr, ('reData', ['username']))[0]
                passwd = glom(jsonstr, ('reData', ['password']))[0]
                proxies = f"http://{uname}:{passwd}@{key}"
                return proxies


def get_proxies(change_proxy=False):
    """ get_proxies """
    ip = GetProxies().getproxy(change_proxy)
    return ip


@retry(stop_max_attempt_number=5, wait_random_min=3000, wait_random_max=7000)
@decorator
def post_html(session, post_url: int, post_data: dict, headers=headers, timeout=30):
    """
    :param session: 传入session对象
    :param post_url: post请求需要的url
    :param headers: 报头信息,config模块默认提供
    :param post_data: post信息 字典类型
    :param timeout:
    :return:
    """

    post_req = session.post(url=post_url, headers=headers, data=post_data, timeout=timeout, proxies=get_proxies())
    if post_req.status_code == 200:
        post_req.encoding = post_req.apparent_encoding
        # time.sleep(random.randint(1, 3))
        return post_req
    # 随机等待1-3s


@retry(stop_max_attempt_number=5, wait_random_min=3000, wait_random_max=7000)
@decorator
def get_response(session, url: str, params=None, headers=headers, timeout=10):
    """get_response"""
    try:
        req = session.get(url=url, headers=headers, params=params, timeout=timeout, proxies=get_proxies())
    except:
        req = session.get(url=url, headers=headers, params=params, timeout=timeout, proxies=get_proxies(True))
    if req.status_code == 200:
        req.encoding = req.apparent_encoding
        # time.sleep(random.randint(1, 3))
        return req
    # 随机等待1-3s


@decorator
def get_html(req):
    """ get_html """
    source = req.text
    return source


@decorator
def get_json(req):
    """ get_json """
    try:
        jsonstr = req.json()
    except:
        source = get_html(req)
        if source.endswith(';'):
            jsonstr = json.loads(source.replace(';', ''))
    return jsonstr
