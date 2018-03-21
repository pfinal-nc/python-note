# -*- coding: UTF-8 -*-
import numpy as np

x = np.empty([3,2], dtype =  int)  
print(x)

a = np.zeros((5,),dtype=int)
print(a)

# 自定义输出类型

b = np.zeros((5,3),dtype=[('x','i4')])
print(b)

# 用1 去填充

c = np.ones(5,dtype=int) 
print(c)

# numpy 的 asarray 方法
