# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 10:00
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 容器.py
# @Software: PyCharm
# Python附带一个模块，它包含许多容器数据类型，名字叫作collections
from collections import namedtuple
from enum import Enum


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
# Animal = namedtuple('Animal', 'name age type')
# perry = Animal(name="perry", age=31, type="cat")
#
# print(perry)
# print(perry.name)

#  可以用名字来访问 nametuple 中的数据, 继续分析它,一个命名元组 namedtuple 有两个必须的参数. 他们是元组名称和字段名称. 在上面的代码中, 元组名称是 animal 字段名称是 name, age, type。
#
# animal = namedtuple('Animal', 'name age type')
# perry = animal(name='perry', age=31, type='cat')
# print(perry[0], perry[1], perry[2])
# # 将一个命名元组转换为字典
# print(perry._asdict())

# enum.Enum 枚举对象

class Species(Enum):
    """Species"""
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推
    kitten = 1
    puppy = 2


animal = namedtuple('Animal', 'name age type')
perry = animal(name='perry', age=31, type=Species.cat)
drogon = animal(name='drogon', age=3, type=Species.dragon)
tom = animal(name='tom', age=2, type=Species.cat)
charlie = animal(name='charlie', age=1, type=Species.cat)

print(charlie.type == tom.type)
