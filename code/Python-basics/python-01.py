# -*- coding: utf-8 -*-
s = 'string'
print (45678 + 0x12fd2 )

print ("this is python demo")

# 这个是闹着玩的
print ("100+100 =",100+100)

# #############################

x =35 
y =24

print (x*y)

e=10

e = e+2;

print (e);

# 等擦数列

x100 = 100;

print (r"'''''");

print ('''
daye wo hao nanguo 
	''');

# 输出中文

print ( u"中文"); # 这是中文编码

# ----------
print ((1+2)*3);

print( 2.5 + 10 /4 );

print(True and False);
print(not False);

# python list
l = [1,2,3,4];
print(l[-2]);

# list添加值
l.append('大爷的');
print(l)

l.insert(0,'蛋疼');
print(l);

# 
l.pop();
print(l);
l.pop(2);
print(l);

# 
l[1]='这个是闹着玩的';
print(l);

# 
t = (1,2,3,)
print(t);

#
L = ('a','b',['A','B']);
print(L[2]);

# if 语句
age = 20;

if age > 10:
	print(age);
else:
	print('大爷');

# if elif 语句

if age >30 :
	print('这个是大爷的');
elif age > 25:
	print('这个是闹着玩的');
elif age > 20:
	print('这个我不知道');
else:
	print('这个你看着办吧');

#	
test = 18;
if test >=6:
	print('dd');
elif test >=18:
	print('adult');
else:
	print('kid');


# for 
L = ['A','B','C','D'];

C = ['A','D',['e','f','b']]

for name in L:
	print(name);

for name in C:
	print(name);

# while

N = 10;
x = 0;
while  x < N:
	print(x);
	x = x+1

sum = 0;
x = 1;
while True:
	sum = sum + 1
	x = x+1;
	if x >100:
		break

print(sum);

# for 与 for 嵌套

for x in ['A','B','C','D']:	
	for y in ['1','2','3']:	
		print(x + y)	

#dict {}
d = {
	'Admin' :95,
	'Admin' :92,
	'Admin2' :95,	
};
print(d);

#len()
print(len(d));
print(len(L));


