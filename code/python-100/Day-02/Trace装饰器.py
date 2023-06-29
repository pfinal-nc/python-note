# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 17:41
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : Trace装饰器.py
# @Software: PyCharm
import linecache
import os
import sys


def trace(f):
    def globaltrace(frame, why, arg):
        if why == "call": return localtrace
        return None

    def localtrace(frame, why, arg):
        if why == "line":
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print("{}({}): {}".format(bname, lineno, linecache.getline(filename, lineno)))
        return localtrace

    def _f(*args, **kwargs):
        sys.settrace(globaltrace)
        result = f(*args, **kwargs)
        sys.settrace(None)
        return result

    return _f


@trace
def test():
    print(1)
    print(2)
    print(3)

test()