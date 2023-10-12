# python 技巧

# def get_user(user):
#     """ get user """
#     if user:
#         return user
#     return "匿名用户"

# 使用短路运算处理, 需要一行代码即可
#
# def get_user(user):
#     """ get user """
#     return user or "匿名用户"

# 切片替代循环 (slice)

# 使用切片替代循环或递归来操作序列, 切片是一种用于从一个序列(字符串, 列表，元组等) 中获取一部分或全部元素的语法

# 使用循环
# def reverse(lst):
#     """ reverse """
#     new_lst = []
#     for i in range(len(lst) - 1, -1, -1):
#         new_lst.append(lst[i])
#     return new_lst
#
#
# lst = [1, 2, 3, 4, 5]
# print(reverse(lst))  # [5, 4, 3, 2, 1]
#
#
# # 使用切片
# def reverse(lst):
#     return lst[::-1]
#
#
# lst = [1, 2, 3, 4, 5]
# print(reverse(lst))  # [5, 4, 3, 2, 1]
#
# # 列表推导式 (list comprehension)
# # 列表推导式是一种用于从一个可迭代对象(如列表, 元组, 字典, 集合等) 创建一个新的列表的简洁的语法
#
# # 使用普通的循环
# lst = [1, 2, 3, 4, 5, 6]
# new_lst = []
# for x in lst:
#     if x % 2 == 0:
#         new_lst.append(x * 2)
# print(new_lst)
#
# # 使用列表推导式
# lst = [1, 2, 3, 4, 5, 6]
# new_lst = [x * 2 for x in lst if x % 2 == 0]
# print(new_lst)
#
# # 生成器表达式
#
# # 生成器表达式 是 一种类似于列表推导式的语法, 但是它不会一次性生成一个完整的列表. 而是返回一个生成器对象, 可以按需逐个产生元素
#
# # 使用普通的循环
# lst = [1, 2, 3, 4, 5, 6]
# sum = 0
# for x in lst:
#     if x % 2 == 0:
#         sum += x ** 2
# print(sum)

# 使用生成器表达式
lst = [1, 2, 3, 4, 5, 6]
sumsum = sum(x**2 for x in lst if x % 2 == 0)
print(sumsum)
# 在生成器表达式可以节省内存空间, 提高性能, 适合处理大量或无限的数据,而且不会占用额外的内存空间,特别使用于读取大批量的数据. 当然我们也可以用yeild 也能做一个生成器

# 枚举 (enumerate)
# 枚举是一种用于同时获取可迭代对象中的元素和索引的函数. 枚举可以避免使用额外的变量来记录索引, 提高了代码的可读性和效率

# 使用浦东的循环
lst = ["a", "b", "c", "d", "e"]
index = 0
for x in lst:
    print(index, x)
    index += 1
# 使用枚举的代码更加简洁和清晰，而且不需要手动更新索引
for index, x in enumerate(lst):
    print(index, x)
# 三元运算符 (Ternary Operator)
# 三元运算符是一种用于根据一个条件表达式来选择两个不同的值的简洁的语法
num = -5
if num > 0:
    sign = "positive"
else:
    sign = "negative"
print(sign)

sign = "positive" if num > 0 else "negative"

print(sign)


#  字典处理条件判断
#  遇到if 循环语句很长的时候,其实可以使用字典来替代, 两者的执行效率没有试验过


# 使用多个if-elif-else 语句
def foo(x):
    """foo"""
    if x == "a":
        return 1
    elif x == "b":
        return 2
    elif x == "c":
        return 3
    else:
        return -1


print(foo("a"))


# 使用字典
def foo(x):
    """foo"""
    dic = {"a": 1, "b": 2, "c": 3}
    return dic.get(x, -1)


print(foo("a"))

# 装饰器 (decorator)

# 装饰器是一种用于在不修改原函数定义和调用的情况下, 给函数添加额外的功能或修改其行为的语法

# 使用普通的函数调用
# import time
#
#
# def foo():
#     # do something
#     time.sleep(1)
#
#
# start = time.time()
# foo()
# end = time.time()
# print(f"foo() took {end - start} seconds to run.")

# 使用装饰器
#
# def timer(func):
#     """timer """
#
#     def wrapper(*args, **kwargs):
#         """ wrapper """
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__}() took {end - start} seconds to run.")
#         return result
#
#     return wrapper
#
#
# @timer  # 相当于 foo = timer(foo)
# def foo():
#     """foo"""
#     time.sleep(1)
#
# foo()

# 上下文管理器 (context manager)
# 上下文管理器是一种用于在执行某些操作之前和之后自动执行一些预设的操作的语法, 上下文管理器可以用于实现一些资源管理的功能

# 使用普通的try-finally语句
# file = open("test.txt", "r")
# try:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# 使用上下文管理器
# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)
