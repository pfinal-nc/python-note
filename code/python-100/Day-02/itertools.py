# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 18:01
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : itertools.py
# @Software: PyCharm
import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)

print(races)
print(list(itertools.permutations(horses)))
