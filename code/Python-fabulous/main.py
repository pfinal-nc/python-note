# -*- coding: utf-8 -*-

from weibo.weibo_login import wblogin
import weibo.weibo_fabulous
# from weibo.weibo_qrcode import wblogin
import time

if __name__ == '__main__':
    (wei_session, uid) = wblogin()
    if uid is not None:
        weibo.weibo_fabulous.get_profile_list(wei_session,['7197765669'])

    # print(result)
