# -*- coding: UTF-8 -*-

a = [99,66,25,10,3]

print(range(len(a)/2));

if __name__ == '__main__':
    N = len(a)
    print a
    for i in range(len(a) / 2):
        a[i],a[N - i - 1] = a[N - i -1],a[i]
    print(a)

