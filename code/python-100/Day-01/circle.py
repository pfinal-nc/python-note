#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import math

radius = float(input('请输入圆的半径:'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('圆的周长:%.2f' % perimeter)
print('圆的面积:%.2f' % area)
