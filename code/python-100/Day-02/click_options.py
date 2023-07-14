# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 11:12
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_options.py
# @Software: PyCharm
# option 最基本的用法就是好通过指定命令行选项的名称, 从命令读取参数值, 再将其传递给函数
# option 常用的设置参数如下：
# default: 设置命令行参数的默认值
# help: 参数说明
# type参数类型，可以是 string, int, float 等
# prompt: 当在命令行中没有输入相应的参数时，会根据 prompt 提示用户输入
# nargs: 指定命令行参数接收的值的个数
# metavar：如何在帮助页面表示值
import click


# 指定 type

@click.command()
@click.option('--rate', type=float, help='rate')  # 指定 rate是float 类型
def show(rate):
    click.echo('rate %s' % rate)


if __name__ == '__main__':
    show()
