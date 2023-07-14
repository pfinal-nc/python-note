# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 11:28
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_intrange.py
# @Software: PyCharm
import click


@click.command()
@click.option('--count', type=click.IntRange(0, 20, clamp=True))
@click.option('--digit', type=str, default='#')
def repeat(count, digit):
    click.echo(str(digit) * count)


if __name__ == '__main__':
    repeat()
