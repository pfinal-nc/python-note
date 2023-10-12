# -*- coding: utf-8 -*-
# @Time    : 2023/10/7 17:10
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : pytest_01.py
# @Software: PyCharm
import pytest


# def test_passing():
#     assert (1, 2, 3) == (1, 2, 3)


# 捕获异常
# def test_raises():
#     with pytest.raises(TypeError) as e:
#         connect('localhost', 6379)
#     exec_msg = e.value.args[0]
#     assert exec_msg == 'port type must be int'

# 标记函数
# 默认情况下 pytest 会递归查找当前目录下所有 test 开始或结尾的  python 脚本. 并执行文件内的所有 test开始或结束的函数和方法
# @pytest.mark.finished
# def test_func1():
#     assert 1 == 1


# 由于某种原因 test_func2 功能未完成 只想执行指定函数 在pytest 中有几种方式可以解决
# 1. 通过 :: 显示指定  pytest 01.py::test_func1
# 2. 使用模糊匹配，使用 -k 选项标识。
# 3. 使用 pytest.mark 在函数上进行标记
# @pytest.mark.unfinished
# def test_func2():
#     assert 1 != 1

#  跳过测试
# @pytest.mark.skip(reason="先跳过")
# def test_func2():
#     assert 1 != 1

# 预见的错误
#  事先知道测试函数会执行失败, 但有不想直接跳过, 而是希望显示的提示  python 使用 pytest.mark.xfail 事先遇见错误功能

# @pytest.mark.xfail(gen.__version__ < '0.2.0',reason='not supported until v0.2.0')
# def test_api():
#     id_1 = gen.unique_id()
#     id_2 = gen.unique_id()
#     assert id_1 != id_2

# 参数化
# 当对一个测试函数进行测试时 通常会给喊出传递多组参数. 比如 测试账号登录, 需要模拟个钟千奇百怪的账号密码 当然，我们可以把这些参数写在测试函数内部进行遍历。不过虽然参数众多，但仍然是一个测试，当某组参数导致断言失败，测试也就终止了。
# 当然，我们可以把这些参数写在测试函数内部进行遍历。不过虽然参数众多，但仍然是一个测试，当某组参数导致断言失败，测试也就终止了。
# 通过异常捕获, 可以保证程所有参数完整执行, 但要分析测试结果就需要做不少额外的 工作.
# 在pytest 中, 有更好的解决方法, 就是参数化测试, 即每组参数都独立执行一次测试。使用的工具就是 pytest.mark.parametrize(argnames, argvalues)。

# @pytest.mark.parametrize('passwd', ['123456', 'abcdefdfs', 'as52345fasdf4'])
# def test_passwd_length(passwd):
#     assert len(passwd) >= 8


# 检验用户密码
@pytest.mark.parametrize("user, passwd", [("jack", "abcdefgh"), ("tom", "a123456a")])
def test_passwd_md5(user, passwd):
    db = {
        "jack": "e8dc4081b13434b45189a720b77b6818",
        "tom": "1702a132e769a623c1adb78353fc9503",
    }

    import hashlib

    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]
