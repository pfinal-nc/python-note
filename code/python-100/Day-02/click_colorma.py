# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 13:38
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_colorma.py
# @Software: PyCharm
import click


@click.command()
@click.option('--name', help='The person to greet.')
def hello(name):
    click.secho('Hello %s' % name, fg='red', underline=True)
    click.secho('Hello %s' % name, fg='green')


# fg 表示前景颜色（即字体颜色），可选值有：BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE 等；
# bg 表示背景颜色，可选值有：BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE 等；
# underline 表示下划线，可选的样式还有：dim=True，bold=True 等；

if __name__ == '__main__':
    hello()

# click 通过 click.option() 添加可选参数, 通过哦 click.argument() 来添加有可能可选的参数

