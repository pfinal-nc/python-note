# -*- coding: utf-8 -*-
# @Time    : 2023/9/25 14:12
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 极简代码.py
# @Software: PyCharm
import sys
from collections import Counter


#  重复元素判定

def all_unique(lst):
    """ all_unique"""
    return len(lst) == len(set(lst))


#  字符串元素组成判定

def anagram(first, second):
    """ anagram(first, second)"""
    return Counter(first) == Counter(second)


# 字节占用

def byte_size(string):
    """" byte_size()"""
    return len(string.encode('utf-8'))


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 1, 2, 9, 0]
    y = [3, 4, 5, 6, 7, 1, 2]
    print(all_unique(x))
    print(all_unique(y))

    print(anagram("abcd3", "3acdd"))

    # 内存占用
    variable = 30
    print(sys.getsizeof(variable))  #

    print(byte_size(" "))
