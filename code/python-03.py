# 导入数学函数库
import math

#print(math.cos(1));

def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)	

print(fact(1));

L = ['Admin','Lisa','Bart','Paul'];

for index, name in enumerate(L):
	print(index,'---',name);

print('-------------------');

for index, name in zip(range(1,len(L)+1),L):
	print(index,'--',name);

print('-------------------');

d = {'admin':95, 'Lisa':85, 'Bart':59,'Paul':74}
sum = 0.0

for v in d.itervalues():
	sum = sum + v
print(sum / len(d));

print('===================');

print(join(L));