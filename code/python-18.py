from collections import *
'''
from collections import namedtuple
from collections import deque
from collections import defaultdict
'''
# 表示一个点
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)

# 表示一个圆
Circle = namedtuple('Cricle',['x','y','c'])
p = Circle(1,2,6)
print(p.c);

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

q = deque(['a','b','c'])
q.append('x')
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

dd = defaultdict(lambda:'大爷的')
dd['key1']='这个不知道'
print(dd['key1'])
print(dd['key2'])

# Counter是一个简单的计数器，例如，统计字符出现的个数：

c = Counter()
for ch in 'programming':
    c[ch]+=1

print(c)