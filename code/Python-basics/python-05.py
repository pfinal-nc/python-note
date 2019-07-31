import sys;
print("=========Python =============");
print('命令行参数:')
#for i in sys.argv:
#	print(i)
#print('\n Python的路径',sys.path)


# help(max);
counter = 100
miles = 1000.0

print(miles);

# number 类型
a = 111
print(isinstance(a,int))
print(type(a))
print("=============");

# string
c = '这个真的好难过'
print(c);
print(c[3])
print(c[2:])
print(c * 2)
print(c + 'test')

# set 运算
b = set('abcdef')
d = set('cdefadgh')

print(b - d)
print(b | d)
print(b & d)
print(b ^ d)

# 字典
print({x: x**2 for x in (2, 4, 6)})

print("============");


# 数据类型转换

e = 'aaa'

print(float(e))



# is 和 is not  运算符  id() 函数用于获取对象内存地址。
'''
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

























