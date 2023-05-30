# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 16:05
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 优美的表格.py
# @Software: PyCharm
import prettytable as pt

# 按行添加数据
tb = pt.PrettyTable()
tb.field_names = ['name', 'age', 'height', 'weight']
tb.add_row(['飞兔', 25, 174, 65])
tb.add_row(['autofelix', 23, 164, 55])
tb.add_row(['极客飞兔', 27, 184, 69.5])

print(tb)