# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pfinal'
__mtime__ = '2019/9/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
COVER_RULE = [
    {'#J_UlThumb>li>a>img', '#J_UlThumb > li:nth-child(%d)  > a > img'},
    {'#J_UlThumb>li', '#J_UlThumb > li:nth-child(%d) > a > img'},
    {'#J_UlThumb>li>div>a>img', '#J_UlThumb > li:nth-child(%d)>div > a > img'}
]

DETAILS_RULE = [
    {'#description > div > p', '#description > div > p > img:nth-child(%d)'},

]
