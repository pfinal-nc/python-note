# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 10:00
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 容器.py
# @Software: PyCharm
# Python附带一个模块，它包含许多容器数据类型，名字叫作collections
from collections import namedtuple

# defaultdict
# defaultdict与dict 类型不同, 不需要检查key是否存在

# colours = (
#     ('PFinal', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#
# favorite_colours = collections.defaultdict(list)
# print(favorite_colours)
#
# for name, colour in colours:
#     favorite_colours[name].append(colour)
#
# print(favorite_colours)

# some_dict = {}
# some_dict['colours']['favorite'] = 'yellow'
# 在python 字典嵌套的时候 如果 key不存在则报错,所以可以使用defaultdict 来处理
# tree = lambda: collections.defaultdict(tree)
# print(tree)
# some_dict = tree()
# some_dict['colours']['favorite'] = 'yellow'
# print(some_dict)
# print(json.dumps(some_dict))

############################################################################################################################################################################################################################################################################################################

# counter
# counter 是一个计数器,可以帮助针对某项数据进行计数， 比如它可以用来计算
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#
# favs = Counter(name for name, colour in colours)
# print(favs)

##############################

# deque
# deque 提供了一个双端队列, 可以从/尾两端添加或删除元素
# d = deque()
# d.append('1')
# d.append('2')
# d.append('3')
# d.append('4')
# print(len(d))
# print(d[0])
# print(d[-1])

# 从两端取出 pop 数据
# d = deque(range(5))
# print(len(d))
#
# d.popleft()
# print(d)
#
# d.pop()
# print(d)

# 限制列表的大小,当超出设定的限制时, 数据会从队列另一端被挤出
# d = deque([1, 2, 2, 43, 5], maxlen=5)
# d.extendleft([21])
# d.extend([22, 3, 4])
# print(d)

# namedtuple
# 一个元组是一个不可变的列表,可以存储一个数据的序列 它和命名元组(nametuple)非常像
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
print(perry.name)