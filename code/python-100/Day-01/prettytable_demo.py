# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 09:29
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : prettytable_demo.py
# @Software: PyCharm
from prettytable import PrettyTable, RANDOM, MSWORD_FRIENDLY

# prettytable 命令行输出一个好看的表格

# 传入表头 name,age,country
tb = PrettyTable(["name", "age", "country"])

# 调用 add_row 添加 记录
tb.add_row(["pfinal", 20, "cn"])
tb.add_row(["pfinal", 20, "cn"])
tb.add_row(["pfinal", 20, "cn"])
tb.add_row(["pfinal", 20, "cn"])

# 添加一列
tb.add_column('sex', [1, 1, 1, 1])

# 设置样式
# tb.set_style(MSWORD_FRIENDLY)

print(tb)
