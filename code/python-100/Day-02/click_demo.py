# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 10:57
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_demo.py
# @Software: PyCharm
import click


# 使用Click 分为两个步骤：
# 使用 @click.command() 装饰一个函数，使之成为命令行接口；
# 使用 @click.option() 等装饰函数，为其添加命令行选项等。

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
