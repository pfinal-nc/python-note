# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 11:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : beautiful_code.py
# @Software: PyCharm
# 首字母大写
s = "programming is awesome"
print(s.title())

# 列表合并
a = [1, 2, 3]
b = [4, 5, 6, 7]
print(a + b)
a.extend(b)
print(a)
# 合并列表 +  相对于 extend 要慢一点


# 列表元素去重
a = [1, 2, 3, 4, 2, 3, 5]
print(list(set(a)))
