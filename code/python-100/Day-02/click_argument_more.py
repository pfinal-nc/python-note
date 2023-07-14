# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 11:51
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_argument_more.py
# @Software: PyCharm
import click


# 不定参数
# @click.command()
# @click.argument('x')
# @click.argument('y')
# @click.argument('z')
# def show(x, y, z):
#     click.echo('x: %s y: %s z: %s' % (x, y, z))

@click.command()
@click.argument('src', nargs=1)
@click.argument('dst', nargs=-1)
def move(src, dst):
    click.echo('move %s to %s' % (src, dst))


# 其中，nargs=-1 表明参数 src 接收不定量的参数值，参数值会以 tuple 的形式传入函数。
# 如果 nargs 大于等于 1，表示接收 nargs 个参数值，上面的例子中，dst 接收一个参数值。


if __name__ == '__main__':
    # show()
    move()
