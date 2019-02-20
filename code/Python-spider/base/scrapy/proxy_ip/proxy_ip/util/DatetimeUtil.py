# -*- coding:utf-8 -*-

import time


def get_current_localtime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())