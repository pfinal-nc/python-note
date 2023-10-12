# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 17:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_06.py
# @Software: PyCharm
import pytest


# 参数化
# 固件参数化需要使用 pytest内置的固件 request 并通过 request.params 获取参数


@pytest.fixture(params=[("redis", "6379"), ("elasticsearch", "9200")])
def param(request):
    """param"""
    return request.param


@pytest.fixture(autouse=True)
def db(param):
    """db"""
    print("\nSucceed to connect %s:%s" % param)

    yield

    print("\nSucceed to close %s:%s" % param)


def test_api():
    assert 1 == 1
