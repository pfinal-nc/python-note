# -*- coding: UTF-8 -*-

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

year = int(raw_input('请输入年份:\n'));
month = int(raw_input('请输入月份:\n'));
day = int(raw_input('请输入天:\n'));

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <=12:
    num = months[month - 1]
else:    
    print 'date error'
num +=day
# print(num)
# 判断是否是闰年
leap = 0
if (year % 400 == 0 ) or ((year % 4 == 0 )) and (year % 100 != 0):
    leap = 1
if (leap==1) and (month > 2) :
    num += 1
print('it os the %dth day.' % num)