# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 13:55
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 正则表达式.py
# @Software: PyCharm
import re

##### 基本匹配规则 #####
# pattern = r'abc'  # 匹配字符串"abc"
# string = "xyz abc def"
#
# result = re.findall(pattern, string)
# print(result)

################ 字符类和预定义字符类 ##################

pattern = r"[0-9]"
string = "abc 123 def"
result = re.findall(pattern, string)
print(result)

################## 量词和贪婪匹配 ##############

pattern = r"a+"  # 匹配一个或多个连续的字符 "a"
string = "aaaaabbbbb"
result = re.findall(pattern, string)
print(result)

####################### 边界匹配 ###########################

# pattern = r'\bhello\b'  # 匹配整个单词 "hello"
# pattern = r'\bwo'
pattern = r'o\b'
string = "hello world"

result = re.findall(pattern, string)
print(result)

###################### re.search() ############################

# re.search 方法用于在字符串中搜索匹配模式, 如果任意位置的匹配, 则返回一匹配对象, 否则返回None

pattern = r"world"
string = "hello world"

result = re.search(pattern, string)

if result:
    print("Match found")
else:
    print("No match")

######################## re.sub() ##########################
# re.sub() 方法用于在字符串中搜索匹配模式的子串, 并将其替换为指定的字符串
pattern = r"apple"
string = "I have an apple"

result = re.sub(pattern, "banna", string)
print(result)

####################### 分组和捕获 ###########################
pattern = r"(\d+)-(\d+)-(\d+)"  # 匹配日期格式 "YYYY-MM-DD"
string = "Today is 2023-06-28."

result = re.search(pattern, string)

if result:
    year = result.group(1)
    month = result.group(2)
    day = result.group(3)
    print(f"Year: {year}, Month: {month}, Day: {day}")
else:
    print("No match")

######################## 非贪婪匹配 ##########################
# 非贪婪匹配是指尽可能少地匹配字符
pattern = r"a+?"
string = "aaaaa"

result = re.findall(pattern, string)
print(result)

######################### 向前界定和向后界定 #########################
# 向前界定和向后界定用于限定匹配的前后条件，但不包括在匹配结果中
pattern = r"(?<=@)\w+"  # 匹配邮箱地址中的用户名
string = "john@example.com"

result = re.findall(pattern, string)
print(result)


