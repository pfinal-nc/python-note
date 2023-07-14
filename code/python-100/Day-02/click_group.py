# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 11:06
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_group.py
# @Software: PyCharm
import click


@click.group()
def cli():
    pass


@click.command()
def initdb():
    click.echo("Initialized the database")


@click.command()
def dropdb():
    click.echo('Droped the database')


cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()
