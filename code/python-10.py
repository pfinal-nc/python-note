# -*- coding: utf-8 -*-
#!/usr/bin/python3

L = []
n = 1

while n <=99:
    L.append(n)
    n = n + 2
'''
print(L[0:3])
print(L[:3])
print(L[3:])
print(L[-3])
print(L[-3:])
print(L[:-3])
'''

L1 = list(range(100))
# print(L1[::5])

# print('ABCDEF'[:3])

for key in L1.items():
    print(key)

