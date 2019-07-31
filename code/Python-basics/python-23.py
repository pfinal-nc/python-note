# python 常用函数
# print(help(1))  # 在线帮助

print(callable(int)) # 查看一个obj是不是可以像函数一样调用

# map 函数

def square(n):
    return n * n

print(square(4))

number = [1,2,3,4,5]
li = map(square,number)
print(list(li))

# 