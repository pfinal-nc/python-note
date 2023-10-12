# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 09:46
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_03.py
# @Software: PyCharm
import pytest


# 预处理和后处理

# 很多时候 在测试前 进行预处理(如新建数据库连接），并在测试完成进行清理（关闭数据库连接）。 当有大量重复的这类操作, 最佳实践是使用固件来自动化所有预处理和后处理

# Pytest 使用 yield 关键词将固件分为两部分，yield 之前的代码属于预处理，会在测试前执行；yield 之后的代码属于后处理，将在测试完成后执行。

# @pytest.fixture()
# def db():
#     """db """
#     print("connect successfully")
#
#     yield
#
#     print("connect closed")
#
#
# def search_user(userid):
#     """search user"""
#     d = {
#         "001": "pfinalclub"
#     }
#     return d[userid]
#
#
# def test_search(db):
#     assert search_user("001") == "pfinalclub"

# 作用域
# 固件的作用是为了抽离出重复的工作和方便复用, 为了更精细化控制固件（比如只想对数据库访问测试脚本使用自动连接关闭的固件）pytest 使用作用域来进行指定固件的使用范围
# 在定义固件时，通过 scope 参数声明作用域，可选项有

# 1. function 函数级 每个测试函数都会执行一次固件
# 2. class 类级别 每个测试类执行一次, 所有方法都可以使用
# 3. module 模块级 每个模块执行一次, 模块内函数和方法都可以使用
# 4. session 会话级 一次测试只执行一次, 所有被找到的函数和方法都可用

# @pytest.fixture(scope='function')
# def func_scope():
#     """func_scope"""
#     pass
#
#
# @pytest.fixture(scope='module')
# def mod_scope():
#     """ mod_scope"""
#     pass
#
#
# @pytest.fixture(scope='session')
# def sess_scope():
#     """ sess_scope"""
#     pass
#
#
# @pytest.fixture(scope='class')
# def class_scope():
#     """class_scope"""
#     pass
#
#
# def test_multi_scope(sess_scope, mod_scope, func_scope):
#     """test_multi_scope """
#     pass


# 对于类使用作用域 需要使用 pytest.mark.usefixtures
@pytest.mark.usefixtures("class_scope")
class TestClassScope:
    """test_class_scope"""

    def test_1(self):
        pass

    def test_2(self):
        pass
