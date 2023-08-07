# -*- coding: utf-8 -*-
# @Time    : 2023/8/7 16:18
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : class装饰器.py
# @Software: PyCharm

#
class D(object):
    def __init__(self, a=None):
        self.a = a
        self.mode = "装饰"

    def __call__(self, *args, **kwargs):
        if self.mode == "装饰":
            self.func = args[0]  # 默认第一个参数是被装饰的函数
            self.mode = "调用"
            return self
        # 当self.mode == "调用"时，执行下面的代码（也就是调用使用类装饰的函数时执行）
        if self.a:
            print("欢迎来到{}页面。".format(self.a))
        else:
            print("欢迎来到首页。")
        self.func(*args, **kwargs)


@D()
def index(name):
    print("Hello {}.".format(name))


@D("电影")
def movie(name):
    print("Hello {}.".format(name))


if __name__ == '__main__':
    index("Andy")
    movie("Andy")


