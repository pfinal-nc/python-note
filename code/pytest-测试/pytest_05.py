# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 14:13
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_05.py
# @Software: PyCharm
import pytest


# 重命名
# 固件的名称默认定义时的函数名, 如果不想使用默认, 可以通过 name 选项指定名称:


@pytest.fixture(name="age")
def calculate_age():
    """calculate age"""
    return 28


def test_age(age):
    assert age == 28
