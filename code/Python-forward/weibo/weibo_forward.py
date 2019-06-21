import requests
import time
import re
import json
from config import WBCLIENT, USER_AGENT
from config import USER_NAME, PASSWD

session = requests.session()
session.headers['User-Agent'] = USER_AGENT
FORWARD_URL = "https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100505&__rnd=%d" % int(time.time() * 1000)
RESOURCE_URL = "https://weibo.com/u/%d?is_all=1"


def get_mid_list(wei_session, uid):
    blog_list = wei_session.get(RESOURCE_URL % int(uid))
    pattern = r'\s+action-data=\\"allowForward=1&url=https:\\\/\\\/weibo.com\\\/' + uid + '\\\/\w+&mid=(\d+)'
    blog_list_mid = re.compile(pattern)
    mid_list = re.findall(blog_list_mid, blog_list.text)
    return mid_list


def set_resource_list(wei_session, mids, uid, num=1):
    if len(mids) <= 0:
        return False
    for mid in mids[:num]:
        forward_data = {
            'pic_src': '',
            'pic_id': '',
            'appkey': '',
            'style_type': 1,
            'mark': '',
            'reason': '太赞了 [赞啊]',
            'location': 'page_100505_home',
            'pdetail': '1005057197765669',
            'module': '',
            'page_module_id': '',
            'refer_sort': '',
            'is_comment_base': 1,
            'rank': 0,
            'rankid': '',
            'isReEdit': False,
            '_t': 0,
            'mid': int(mid)
        }
        wei_session.headers['Referer'] = 'https://weibo.com/u/%d?is_all=1' % int(uid)
        res = wei_session.post(FORWARD_URL, data=forward_data)
        result = json.loads(res.text)
        if result['msg'] == '':
            time.sleep(2)
            # print('转发成功')
        else:
            continue
