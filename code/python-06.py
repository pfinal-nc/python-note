#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(len("中国"));

print("==============");

print('''中国人名''');

print("hi, %s 是我的媳妇 "%('王菜菜'));

print('占地 %d%%'%(70))

print("=====");
r = (85-72)/72;
print("%.1f%%"%(r * 100))

print("=======");

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
# classmates[0] = 'Adam'

s = input("s:")
print(s);
s = int(s);
if s<100:
	print('大爷');
elif s<150:
	print('大个');
else:
	print('肚子痛');