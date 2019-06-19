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

USER_INFO_URL = "https://weibo.com/%s/profile?is_all=1&page=%s"
ADD_PROFILE_URL = "https://weibo.com/aj/v6/like/add?ajwvr=6&__rnd=%d" % int(time.time() * 1000)


def get_profile_list(wei_session, uids=[]):
    pattern = r'\s+class=\\"S_txt2\\"\s+action-type=\\"fl_like\\"\s+action-data=\\"(.*?)\\"'
    if len(uids) > 0:
        for uid in uids:
            # print(USER_INFO_URL % uid)
            page = 1
            while page < 5:
                result = wei_session.get(USER_INFO_URL % (uid, page))
                # print(result.text)
                profile_list = re.compile(pattern)
                profile_data = re.findall(profile_list, result.text)
                set_profile(wei_session, profile_data, uid)
                page += 1


def set_profile(wei_session, profile_data, uid):
    wei_session.headers["Referer"] = "https://weibo.com/u/%s?is_all=1" % uid
    if len(profile_data) > 0:
        for params in profile_data:
            params_list = dict([(key, val[0]) for key, val in parse.parse_qs(params).items()])
            # print(params_list)
            res = wei_session.post(ADD_PROFILE_URL, data=params_list)
            print(json.loads(res.text))
            time.sleep(5)
