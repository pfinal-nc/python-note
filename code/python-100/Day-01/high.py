# -*- coding: utf-8 -*-
# @Time    : 2023/10/12 13:39
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : high.py
# @Software: PyCharm
import pymongo


# 设置全局变量
# 设置全局变量的需求并不是直接赋值, 而是想从某个数据结构li引用生成, 可以用下面这两种方法, 推荐第二种, golbals() 支持字典用法很方便.
#
# d = {"a": 1, "b": 2}
# # 粗暴的写法
# # for k, v in d.items():
# #     exec("{}={}".format(k, v))
# #
# # print(d)
# # globals().update(d)
# # print(d)
#
# # 字符串格式化
# # 用format 方法可以支持很多种格式
# print("{key}={value}".format(key="a", value=10))
# print("[{0:<10}], [{0:^10}], [{0:*>10}]".format("a"))  # 左中右对齐
# print("{0[a]}".format(dict(a=10, b=20)))  # 字典
# print("{0.platform}".format(sys))  # 成员
# print("{0[5]}".format(range(10)))  # 列表
# # print("my name is {0} :--{{}}".format('Fred'))  # 真得想显示{} 需要双 {}
# # print("{0!r:20}".format("Hello"))
#
# # 列表去重
# l = [1, 2, 3, 3, 3]
# print(list({}.fromkeys(l).keys()))  # 利用构建字典键去重
# print(list(set(l)))  # 常见 set 函数去重
#
# # 操作字典
# print(dict((["a", 1], ["b", 2])))  # 用两个序列类型构造字典
# print(dict(zip("ab", range(2))))
# print(dict.fromkeys("abc", 1))
#
# # 字典解析
# print({k: v for k, v in zip("abc", range(3))})
#
# d = {"a": 1, "b": 2}
# d.setdefault("a", 100)  # key 存在, 直接返回 value 1
# print(d)
# print(d.setdefault("c", 200))  # key 不存在 先设置 返回 200
# print(d)
#
# # 对字典进行逻辑操作
# # 只能先转成键值对列表再进行操作, 然后转回去
#
# d1 = dict(a=1, b=2)
# d2 = dict(b=2, c=3)
# # print(d1 & d2) 字典不支持该操作
#
# print(d1.items())
# print(d2.items())
# print(dict(d1.items() & d2.items()))  # 交集
# print(dict(d1.items() | d2.items()))  # 并集
# print(dict(d1.items() - d2.items()))  # 差集
# print(dict(d1.items() ^ d2.items()))  # 对称差集
#
# print(('a', 1) in d1.items())  # 判断
#
# # vars 返回对象 object 的属性和属性值的字典对象, 如果没有参数，就打印当前调用位置的属性和属性值,类似 locals()
#
# print(vars() is locals())
#
# # 可用于找类属性
# print(vars(sys) is sys.__dict__)  # 可用于找类属性

# 实现上下文管理类 可以用来自动关闭DB连接

class Operation(object):
    """ Operation """

    def __init__(self, database, host='localhost', port=27017):
        self._db = pymongo.MongoClient(host, port)[database]

    def __enter__(self):
        return self._db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db.connection.disconnect()


with Operation(database='test') as db:
    print(db.test.find_one())
