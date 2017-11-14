print(7 ** 2);

# range() 生成数列
sum = 0;
for x in range(101):
	sum = sum + x;
print(sum);

# dict 字典

L ={
	'key':'值',
	'key1':'值1'
}

print(L);
print(L['key']);
print('key' in L)
print(L.get('key2','默认值'))

# 删除 L 字典中的key1 
# print(L.pop('key1'));
print('key1' in L);

# 数据格式转换  int()  float() bool() str() bool()

a=10;
print(a);

# 函数
def my_count(L):
	a = 0;
	for x in L:
		# print(x);
		a = a + 1
	return a

print(my_count(L));
print(isinstance(L, (int,dict)))