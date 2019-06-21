from weibo.weibo_login import wblogin
import weibo.weibo_forward

if __name__ == '__main__':
    (wei_session, uid) = wblogin()
    mids = weibo.weibo_forward.get_mid_list(wei_session, '7197765669')
    weibo.weibo_forward.set_resource_list(wei_session, mids, '7197765669')
