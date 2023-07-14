# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 11:34
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_sequence.py
# @Software: PyCharm
import click


# is_eager=True 表明该命令行选项优先级高于其他选项；
# expose_value=False 表示如果没有输入该命令行选项，会执行既定的命令行流程；
# callback 指定了输入该命令行选项时，要跳转执行的函数

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--name', default='Ethan', help='name')
def hello(name):
    click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
