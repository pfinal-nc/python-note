# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 11:47
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_argument.py
# @Software: PyCharm
# 使用 @click.option 来添加可选参数，还会经常使用 @click.argument 来添加固定参数
import click


@click.command()
@click.argument('coordinates')
def show(coordinates):
    click.echo('coordinates: %s' % coordinates)


if __name__ == '__main__':
    show()
