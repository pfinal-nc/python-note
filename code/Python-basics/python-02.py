# -*- coding: utf-8 -*-

# if
d = {'a':'c','b':'d'}
if 'a' in d:
	print(d['a']);
print(d.get('a'));

# {}
f = {
	'123':[1,2,3],
	123: '123',
	('a','b'):True
}
print(f);

# for
e = {
	'admin':100,
	'cc':101,
	'dd':'这个是闹着玩的',
	'ee':'这个你看着办吧'
}

for k in e: 
	print(k,'===>',e[k]);

# set
s = set(['a','b','c'])
print(s);
e = ['A','C','D','D','E']
print(set(e))

print('a' in s)

# set 应用

weekdays = set(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])

x = '???'
if x in weekdays:
	print('大爷输入的对');
else:
	print('妹子你输入错误了');

# set 

y = set([('Admin',2),('Admin1',2),('Admin2',2),('Admin3',2)]);

for x in y:
	print(x[0])
y.add('cc');
print(y);
y.remove('cc')
print(y)

# 函数

print (abs(-100));
print(abs(12.34));
print(int(1.2));

def square(L):
	if L >=0:
		return L
	else:
		return -L
print(square(0.1));












