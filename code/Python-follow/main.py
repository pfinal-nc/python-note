# -*- coding: utf-8 -*-

from weibo.weibo_login import wblogin
import weibo.weibo_add_follow
# from weibo.weibo_qrcode import wblogin
import time

if __name__ == '__main__':
    (wei_session, uid) = wblogin()
    uid_list = weibo.weibo_add_follow.weibo_get_search_user(wei_session)
    print(uid_list)
    # print(len(uid_list))
    if len(uid_list) > 0:
        for uid in uid_list:
            time.sleep(1)
            weibo.weibo_add_follow.add_follow(wei_session, int(uid))
    # result = wei_session.get('https://s.weibo.com/user?q=%E5%88%B8&Refer=weibo_user')

    # print(result)
