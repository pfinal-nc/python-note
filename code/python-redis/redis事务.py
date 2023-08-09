# -*- coding: utf-8 -*-
# @Time    : 2023/8/8 16:18
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : redis事务.py
# @Software: PyCharm
# redis 事务是一种原子化操作,可以确保多个redis命令在一个事务中顺序执行, 且执行期间不会受到 其他客户端的干扰， 如果其中任何一个命令失败, 所有命令将被回滚 从而保证事务的一致性
import redis

# 链接reds
r = redis.Redis(host='localhost', port=6379, db=0)

# 创建事务
pipe = r.pipeline()

# 在事务中添加多个命令
pipe.incr('count')
pipe.set('name', 'Alice')
pipe.set('age', 25)

# 执行事务
pipe.execute()

# 获取结果

count = r.get('count')
name = r.get('name')
age = r.get('age')

print(count, name, age)

# 使用Redis事务可以确保多个Redis命令在一个事务中顺序执行，从而保证事务的原子性和一致性，特别是在需要执行多个命令并保持事务的原子性时，使用Redis事务是一种很好的选择

