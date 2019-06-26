import re
import time
import json
from logger import logger
from urllib import parse

FOLLOW_URL = "https://weibo.com/aj/f/followed?ajwvr=6&__rnd=%d" % int(time.time() * 1000)

FOLLOW_USER_URL = "https://weibo.com/%d/follow?rightmod=1&wvr=6"
UID_PAGE = "https://weibo.com/p/%d/myfollow?t=1&cfs=&Pl_Official_RelationMyfollow__95_page=%d"
SEND_MESSAGE = "https://weibo.com/aj/message/add?ajwvr=6&__rnd=%d" % int(time.time() * 1000)
SEARCH_USER_URL = "https://s.weibo.com/user?q=%s&Refer=weibo_user&page=%d"
USER_INFO_URL = "https://weibo.com/u/%s"


def weibo_get_follow_user(wei_session, uid, page=1):
    result = wei_session.get(FOLLOW_USER_URL % int(uid))
    pattern = r"\$CONFIG\[\'page_id\'\]='(\d+)'"
    page_id_p = re.compile(pattern)
    page_id = re.findall(page_id_p, result.text)
    res = wei_session.get(UID_PAGE % (int(page_id[0]), int(page)))
    pattern_u = r'\s+class=\\"member_li S_bg1\\"\s+node-type=\\"user_item\\"\s+action-type=\\"user_item\\"\s+action-data=\\"uid=(\d+)'
    user_ids_p = re.compile(pattern_u)
    user_ids = re.findall(user_ids_p, res.text)
    return user_ids


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


def weibo_get_search_user(wei_session, uid, page=1):
    result = wei_session.get(SEARCH_USER_URL % ('宝妈', int(page)))
    print(result.text)
    pattern_s = r'\s+class="s-btn-c"\s+uid=(\d+)'
    search_uids = re.compile(pattern_s)

    users_ids = re.findall(search_uids, result.text)
    print(users_ids)
    return users_ids


def weibo_send_messages(wei_session, uid, text='互关可好'):
    params = {
        'location ': 'msgdialog',
        'module': 'msgissue',
        'style_id': 1,
        'text': text,
        'uid': uid,
        'tovfids': '',
        'fids': '',
        'el': '[object HTMLDivElement]',
        '_t': 0
    }
    wei_session.headers['Referer'] = 'https://weibo.com/message/history?uid=%d' % int(uid)
    try:
        res = wei_session.post(SEND_MESSAGE, params)
        result_data = json.loads(res.text)
        if result_data['code'] == '100000':
            logger.info('给用户UID%d消息发送成功' % int(uid))
        else:
            logger.info('给用户UID%d消息发送失败' % int(uid))
    except Exception as e:
        logger.debug(e)
        # logger.info('微博[%s]关注失败' % str(params['fnick']))
