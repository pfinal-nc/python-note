# -*- coding: utf-8 -*-
# @Time    : 2023/10/7 18:15
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_02.py
# @Software: PyCharm
import pytest


# 固件 fixture 是一些函数, pytest 会在执行测试函数之前 加载运行他们


@pytest.fixture()
def postcode():
    """
    postcode
    """
    return "010"


def test_postcode(postcode):
    assert postcode == "010"


# pytest 使用文件 conftest.py 集中管理固件
