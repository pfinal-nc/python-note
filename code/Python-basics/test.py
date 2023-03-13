#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def matrix_multiplication(n, A, B):
    C = []
    for line in range(n):
        line_arr = []
        for column in range(n):
            item = 0
            for i in range(n):
                item += A[line][i] * B[i][column]
            line_arr.append(item)
        C.append(line_arr)
    return C

def Fib_matrix_power(n):
    if n < 2:
        return n
    A = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    matrix_n = 2
    while n > 0:
        if n & 1:
            result = matrix_multiplication(matrix_n, result, A)
        A = matrix_multiplication(matrix_n, A, A)
        n //= 2
    return result[0][1]
if __name__ == '__main__':
    print(Fib_matrix_power(9292))
