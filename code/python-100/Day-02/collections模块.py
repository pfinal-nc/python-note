# -*- coding: utf-8 -*-
# @Time    : 2023/8/3 14:01
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : collections模块.py
# @Software: PyCharm
import queue
from collections import namedtuple

#  在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等
# 1.namedtuple 生成可以使用名字来访问元素内容的 tuple
# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
# 3.Counter: 计数器，主要用来计数
# 4.OrderedDict: 有序字典
# 5. defau 队列

# 表示二维坐标
Point = namedtuple("Point", ["x", "y"])

# p = Point(1, 2)
# # 从二维坐标中取 x 轴的数值
# print(p.x, p.y)
#
# # 表示三维坐标
# Point2 = namedtuple("Point2", ["x", "y", "z"])
# p2 = Point2(1, 2, 3)
# # 从二维坐标中取x 轴的数值
# print(p2.x, p2.y, p2.z)
#
# # 创建扑克牌
#
# Card = namedtuple("Card", ["suits_color", "shape", "number"])
# # 生成一张扑克牌
# suits_color = ['red', 'black']
# shape = ['♠', '♦', '♣']
#
# for i in range(3):
#     clo = Card(random.choice(suits_color), random.choice(shape), random.choice(range(2, 10)))
#     # 打印这张扑克
#     # print(clo)
#     # print(clo.suits_color, clo.shape, clo.number)
#     # # 打印这张扑克牌的大小
#     # print(clo.number)
#     cprint(clo.shape + str(clo.number), clo.suits_color)

# queye(队列) 方法
# python 中的queue模块中提供了同步的， 线程安全的队列类, 包括FIFO (先入先出) 队列 Queue LiFO (后入先出) 队列LifoQueue 和 优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。
# 1. queue.put() 向队列中放值
# 2. queue.get() 从队列中取值
# 3. queue.qsize() 返回队列的大小
# 4. queue.empty() 如果丢列为空,返回 True  反之 False
# 5. queue.full() 如果队列满了, 返回 True 反之 False, queue.full 与 maxsize 大小对应
# 6. queue.get([block[, timeout]])获取队列，timeout等待时间
# 7. queue.get_nowait() 相当于Queue.get(False)，非阻塞方法
# 8. queue.put(item) 写入队列, timeout等待时间
# 9. queue.task_done() 在完成一项工作之后, queue.task_done() 函数向任务已经完成的队列发送一个信号。每个get() 调用得到一个任务, 接下来task_done() 调用告诉队列该任务已经处理完毕
# 10.queue.join() 实际上意味着等到队列为空， 再执行别的操作

# 首先创建一个队列
q = queue.Queue()
# 往q 队列中依次放值
q.put(9)
q.put(8)
q.put(7)
# 往队列中依次取值
print(q.get())
print(q.get())
print(q.get())

#  如果不想出现阻塞 可以取值之前用 queue.qsize() 看看队列的大小
# 队列
q.put([1, 2, 3, 4, 5, 6, 7, 8])
q.put(8)
print(q)
