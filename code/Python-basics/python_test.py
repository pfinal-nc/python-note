# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 15:11
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : python_test.py
# @Software: PyCharm
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))

def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
if __name__ == '__main__':
    print(fib(9292))
# def ways(n):
#     A = 3**(n+6)
#     M = A**6 - A**5 - A**4 - A**3 - A**2 - A - 1
#     return pow(A, n+6, M) % A
# if __name__ == '__main__':
#     for i in range(610):
#         print(ways(i))