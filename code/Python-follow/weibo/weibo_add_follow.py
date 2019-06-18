# -*- coding: utf-8 -*-
import requests
import re
from config import WBCLIENT, USER_AGENT
from config import USER_NAME, PASSWD
from logger import logger

session = requests.session()
session.headers['User-Agent'] = USER_AGENT

SEARCH_URL = "https://s.weibo.com/user?q= %s &Refer=weibo_user"


def weibo_get_search_user(wei_session, key='券'):
    result = wei_session.get(SEARCH_URL % (key))
    # print(result.text)
    pattern = r'a\s+href=".*"\s+class="s-btn-c"\s+uid=(\d+)'
    uid_list_pattern = re.compile(pattern)
    uid_list_a = re.findall(uid_list_pattern, result.text)
    return uid_list_a
    # <a href="javascript:void(0);" class="s-btn-c" uid="1642585887" action-type="userFollow" suda-data="key=tblog_search_weibo&amp;value=seqid:15608605889140516327|type:3|t:0|pos:1-0|q:%E5%88%B8|ext:mpos:1,click:user_attend"><i class="wbicon s-color-a">+</i>关注</a>


def add_follow(wei_session,uid):
    # print(uid)
    result = wei_session.get('https://weibo.com/u/' + str(uid))
    # print(result.text)
    pattern = r'\s+class=\\"btn_bed W_fl\\"\s+node-type=\\"focusLink\\"\s+action-data=\\"(.*?)\\"'
    follow_data = re.compile(pattern)
    follow_data_all = re.findall(follow_data, result.text)
    # post 发送到 https://weibo.com/aj/f/followed?ajwvr=6&__rnd=1560870912194
    print(follow_data_all)
