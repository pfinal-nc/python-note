
import re
# 错误异常

try:
    print('try.....')
    r = 10 / 0
    print('result',r)

except ZeroDivisionError as e:
    print('except：',e)
finally:
    pass

# python 的正则表达式
s = 'ABC\\-001'
s1 = r'ABC\-001'
print(s)
print(s1)

''' test = input('输入点啥:');
if re.match(r'^\d+[A-Z]{3,6}$',test):
    print('对的')
else:
    print('大爷你填错了')
'''

# 正则表达式切割字符串

print(re.split(r'[\s\,\:]+','a,b c d:f'))