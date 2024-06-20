# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 下午5:56
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 多装饰器.py
# @Software: PyCharm


def d(a=None):  # 定义一个外层函数，给装饰器传参数--role
    def foo(func):  # foo是我们原来的装饰器函数，func是被装饰的函数
        def bar(*args, **kwargs):  # args和kwargs是被装饰器函数的参数
            # 根据装饰器的参数做一些逻辑判断
            if a:
                print("欢迎来到{}页面。".format(a))
            else:
                print("欢迎来到首页。")
            # 调用被装饰的函数，接收参数args和kwargs
            func(*args, **kwargs)

        return bar

    return foo


@d()
def index(name):
    print("Hello {}.".format(name))


@d("电影")
def movie(name):
    print("Hello {}.".format(name))


class D(object):
    def __call__(self, cls):
        class Inner(cls):
            def f(self):
                print("f")

        return Inner


@D()
class C(object):
    def f(self):
        print("cccc")


if __name__ == '__main__':
    # index("张三")
    # movie("张三")
    c = C()
    c.f()
    list1 = list(range(10))
    list2 = [i+100 for i in list1 if i % 2 == 0 or i % 3 == 0]
    print(list2)