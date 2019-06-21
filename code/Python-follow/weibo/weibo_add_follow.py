# -*- coding: utf-8 -*-
import requests
import re
import json
import time
from urllib import parse
from config import WBCLIENT, USER_AGENT
from config import USER_NAME, PASSWD
from logger import logger

session = requests.session()
session.headers['User-Agent'] = USER_AGENT

SEARCH_URL = "https://d.weibo.com/1087030002_2975_2006_0?page=%s"
# SEARCH_URL = "https://s.weibo.com/user?q=宝妈&Refer=SUer_history&page=%s"
# FOLLOW_URL = "http://weibo.com/aj/f/followed?ajwvr=6&__rnd=1560923446453"
FOLLOW_URL = "https://weibo.com/aj/f/followed?ajwvr=6&__rnd=%d" % int(time.time() * 1000)
USER_INFO_URL = "https://weibo.com/u/%s"


def weibo_get_search_user(wei_session):
    page = 1
    uid_list_a = [];
    while page < 20:
        result = wei_session.get(SEARCH_URL % page)
        # print(result.text)
        pattern = r'span\s+node-type=\\"widget_followBtnBox\\"\s+action-data=\\".*?uid=(\d+)'
        # pattern = r'class="s-btn-c"\s+uid=(.*?)\s+action-type=userFollow'
        uid_list_pattern = re.compile(pattern)
        uid_list_a += re.findall(uid_list_pattern, result.text)
        page += 1

    return uid_list_a
    # <a href="javascript:void(0);" class="s-btn-c" uid="1642585887" action-type="userFollow" suda-data="key=tblog_search_weibo&amp;value=seqid:15608605889140516327|type:3|t:0|pos:1-0|q:%E5%88%B8|ext:mpos:1,click:user_attend"><i class="wbicon s-color-a">+</i>关注</a>


def add_follow(wei_session, uid):
    result = wei_session.get(USER_INFO_URL % uid)
    pattern = r'\s+class=\\"btn_bed W_fl\\"\s+node-type=\\"focusLink\\"\s+action-data=\\"(.*?)\\"'
    oid_pattern = r'\$CONFIG\[\'oid\'\]=\'(.*?)\''
    user_params = re.compile(pattern)
    oid_re = re.compile(oid_pattern)
    (user_params_all,) = re.findall(user_params, result.text)
    (oid,) = re.findall(oid_re, result.text)
    follow_params = parse.parse_qs(
        user_params_all + parse.urlencode({"location": "page_100505_home", "oid": oid, "_t": 0}))
    params = dict([(key, val[0]) for key, val in follow_params.items()])
    wei_session.headers["Referer"] = "https://weibo.com/u/%s?refer_flag=%s" % (params['uid'], params['refer_flag'])
    try:
        res = wei_session.post(FOLLOW_URL, data=params)
        result_data = json.loads(res.text)["data"]
        if result_data:
            logger.info('微博[%s]关注成功' % str(result_data['fnick']))
        else:
            logger.info('微博[%s]关注失败' % str(params['fnick']))
    except Exception as e:
        logger.debug(e)
        logger.info('微博[%s]关注失败' % str(params['fnick']))
