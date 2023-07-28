# -*- coding: utf-8 -*-
# @Time    : 2023/7/28 17:51
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : termcolor_demo.py
# @Software: PyCharm
from termcolor import cprint


def main():
    """ main"""
    title = '''
____________ _             _ _____ _       _     
| ___ \  ___(_)           | /  __ \ |     | |    
| |_/ / |_   _ _ __   __ _| | /  \/ |_   _| |__  
|  __/|  _| | | '_ \ / _` | | |   | | | | | '_ \ 
| |   | |   | | | | | (_| | | \__/\ | |_| | |_) |
\_|   \_|   |_|_| |_|\__,_|_|\____/_|\__,_|_.__/ 
'''
    author = ' '*50 + 'author by : PFinal南丞'
    cprint(title, 'blue')
    cprint(author, 'green')


if __name__ == '__main__':
    main()
