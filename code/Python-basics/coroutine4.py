# -*- coding: utf-8 -*-
# @Time    : 2023/4/7 10:08
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : coroutine4.py
# @Software: PyCharm
def coroutine_example(name):
    print('start coroutine...name:', name)
    x = yield name  # 调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
    print('send值:', x)
    return 'zhihuID: PFinal'


def grouper2():
    result2 = yield from coroutine_example('PFinal')  # 在此处暂停，等待子生成器的返回后继续往下执行
    print('result2的值：', result2)
    return result2


def grouper():
    result = yield from grouper2()  # 在此处暂停，等待子生成器的返回后继续往下执行
    print('result的值：', result)
    return result


def main():
    g = grouper()
    next(g)
    try:
        g.send(10)
    except StopIteration as e:
        print('返回值：', e.value)


# 从上面也可看到yield from起到一个双向通道的作用，同时子生成器也可使用yield from调用另一个子生成器，一直嵌套下去直到遇到yield表达式结束链式。
#
# yield from一般用于asyncio模块做异步IO
if __name__ == '__main__':
    main()
