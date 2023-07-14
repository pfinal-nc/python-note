# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 11:26
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : click_password.py
# @Software: PyCharm
import click


# @click.command()
# @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
# def input_password(password):
#     click.echo('password: %s' % password)

# 通过使用 @click.password_option()，上面的代码可以简写成：

@click.command()
@click.password_option()
def input_password(password):
    click.echo('password: %s' % password)


if __name__ == '__main__':
    input_password()
