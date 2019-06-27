from weibo.weibo_login import wblogin
from weibo.weibo_get_follow_user import weibo_get_follow_user
from weibo.weibo_get_follow_user import weibo_send_messages
from weibo.weibo_get_follow_user import weibo_get_search_user
from weibo.weibo_get_follow_user import add_follow
import time

if __name__ == '__main__':
    (wei_session, uid) = wblogin()
    text = '美女'
    page = 1
    while page <= 5:
        # print(page)
        uids = weibo_get_search_user(wei_session,text,uid, page)
        # print(uids)
        # uids = weibo_get_follow_user(wei_session, uid, page)
        for uid in uids:
            add_follow(wei_session, uid)
            time.sleep(2)
            weibo_send_messages(wei_session, uid)
        page += 1
