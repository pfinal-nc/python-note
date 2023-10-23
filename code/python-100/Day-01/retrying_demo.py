# -*- coding: utf-8 -*-
# @Time    : 2023/10/23 14:40
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : retrying_demo.py
# @Software: PyCharm
import time

from retrying import retry


# retrying 默认是无限重试的
# stop_max_attempt_number 参数 最大重试次数
# stop_max_delay 模拟最大重试时间
# wait_fixed 重试间隔时间
# 1.wait_random_min，重试间隔最小时间  2.wait_random_max，重试间隔最大时间
# stop_func 重试的同事调用一个方法
# retry_on_exception 指定重试的异常类型
# retry_on_result 指定重试的特定条件

def el():
    """el"""
    time.sleep(1)
    print('err')
    raise TypeError


# 全局计数器
a = 1


@retry
def demo1(n):
    """demo1"""
    # 方法中调用全局变量, 需要gloabal
    global a
    # 进行 try-except
    try:
        print(f'开始尝试!{a}')
        a += 1
        el()
    except Exception as e:
        print(e)
        # 当重试完成后还未成功，则返回超时
        raise TimeoutError


# 模拟醉倒重试次数
@retry(stop_max_attempt_number=3)
def demo2():
    """demo2"""
    global a
    # 进行 try-except
    try:
        print(f'开始尝试!{a}')
        a += 1
        el()
    except Exception as e:
        print(e)
        # 当重试完成后还未成功, 则返回超时
        raise TimeoutError


# 模拟最大重试时间
@retry(stop_max_delay=2000)
def demo3():
    """demo3"""
    global a
    # 进行 try-except
    try:
        print(f'开始尝试!{a}')
        a += 1
        el()
    except Exception as e:
        print(e)
        # 当重试完成后还未成功, 则返回超时
        raise TimeoutError


if __name__ == '__main__':
    # demo1(0)
    # demo2()
    demo3()
