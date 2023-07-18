# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 09:56
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_demo01.py
# @Software: PyCharm
from datetime import datetime
from time import sleep
from unittest import TestCase


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)  # 断言


class TestClassDemo(TestCase):
    """Test class demo"""

    def setUp(self):
        """ setup 提前量"""
        print("提前量")
        sleep(1)

    def test_001(self):
        print("用例001", datetime.now())

    def tearDown(self) -> None:
        """ tear down 后置量"""
        print("我是后置", datetime.now())
