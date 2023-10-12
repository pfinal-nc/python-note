# -*- coding: utf-8 -*-
# @Time    : 2023/10/12 13:39
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : high.py
# @Software: PyCharm
import sys

# 设置全局变量
# 设置全局变量的需求并不是直接赋值, 而是想从某个数据结构li引用生成, 可以用下面这两种方法, 推荐第二种, golbals() 支持字典用法很方便.

d = {"a": 1, "b": 2}
# 粗暴的写法
# for k, v in d.items():
#     exec("{}={}".format(k, v))
#
# print(d)
# globals().update(d)
# print(d)

# 字符串格式化
# 用format 方法可以支持很多种格式
print("{key}={value}".format(key="a", value=10))
print("[{0:<10}], [{0:^10}], [{0:*>10}]".format("a"))  # 左中右对齐
print("{0[a]}".format(dict(a=10, b=20)))  # 字典
print("{0.platform}".format(sys))  # 成员
print("{0[5]}".format(range(10)))  # 列表
# print("my name is {0} :--{{}}".format('Fred'))  # 真得想显示{} 需要双 {}
# print("{0!r:20}".format("Hello"))

# 列表去重
l = [1, 2, 3, 3, 3]
print(list({}.fromkeys(l).keys()))  # 利用构建字典键去重
print(list(set(l)))  # 常见 set 函数去重

# 操作字典
print(dict((["a", 1], ["b", 2])))  # 用两个序列类型构造字典
print(dict(zip("ab", range(2))))
print(dict.fromkeys("abc", 1))