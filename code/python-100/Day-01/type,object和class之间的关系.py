# -*- coding: utf-8 -*-
# @Time    : 2023/10/23 17:35
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : type,object和class之间的关系.py
# @Software: PyCharm

# type object和class之间的关系
# type 实例化常见类型
name = 'pfinal'
print(type(name))  # class str
print(type(int))  # class type
print(type(object))  # class type
print(type(type))  # class type

# object 是最顶层基类
print(int.__bases__)  # (<class 'object'>,)
print(type.__bases__)  # (<class 'object'>)
print(object.__bases__)  # ()

# python 常见数据类型
# None(全局只有一个) 即解释器启动时定义
# 迭代类型
# 序列类型 list tuper str bytes
# 集合类型 set frozenset
# 上下文管理类型 with 语句
# 其他: 模块类型, class和实例, 函数类型. 方法类型. 代码类型 object类型 type类型 notimplemented 类型

