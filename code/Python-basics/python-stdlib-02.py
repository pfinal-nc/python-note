# -*- coding: UTF-8 -*-

# num1 = input('输入第一个数字:')
# num2 = input('输入第二个数字:')
# # 求和
# sum = float(num1) + float(num2)
 
# # 显示计算结果
# print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
# print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
for i in range(1,10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i,j,i*j),end='')
    print()
