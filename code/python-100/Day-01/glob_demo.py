# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 10:43
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : glob_demo.py
# @Software: PyCharm
# glob 库是是python 标准库中的一个模块, 提供了一个简单而强大的方法来匹配文件和目录的路径名. 通常情况下, 命令行中使用通配符来搜索文件.
# *.txt 表示匹配所有以 .txt 为后缀的文件.
# glob 库允许以编程的方式在python中执行类似的文件匹配操作.
import fnmatch
import glob
import os

py_files = glob.glob("./*.py")
print(py_files)

# 匹配特定目录
demo_dirs = glob.glob("./../**/*.py")
print(demo_dirs)

# 使用 iglob 进行迭代
py_yielding_files = glob.iglob("*.py")
print(py_yielding_files)  # iglob()返回一个迭代器，逐个返回匹配的文件名。
for file in py_yielding_files:
    print(file)

# 过滤匹配结果
# glob 库允许使用 fnmatch 模块匹配方法来过滤匹配结果. 这对于在匹配结果中执行更复杂的模式匹配非常有用.
file_starting_with_file = fnmatch.filter(glob.glob('*.py'), "day*")  # 匹配以 day开头的文件
print(file_starting_with_file)

# 排序匹配结果
# glob 库返回的匹配结果通常是按照操作系统的文件规则排序的，但是，有时候需要按照指定的方式匹配 结果进行排序

# 获取匹配的文件并按照文件大小排序
matched_files = glob.glob("*.py")
sorted_files_by_size = sorted(matched_files, key=os.path.getsize)
print(sorted_files_by_size)


# 自定义排序规则

def custom_filter(file_path):
    """ custom_filter """
    filename = file_path.split("/")[-1]
    last_char = filename[-4]  # 获取倒数第5个字符，即文件名中的最后一个数字
    return last_char.isdigit() and int(last_char) % 2 == 1


matched_files = glob.glob("*.py")
filtered_and_sorted_files = sorted(filter(custom_filter, matched_files))
print(filtered_and_sorted_files)
