# -*- coding: utf-8 -*-
# @Time    : 2023/4/10 11:48
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : python-24.py
# @Software: PyCharm

# # 生成式(推导式)的用法
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票构造一个新的字典
# prices = {key: value for key, value in prices.items() if value > 100}
# print(prices)

# 嵌套的列表的坑
#
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)
