#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os, sys

Find = {
    'Type': '',
    'Color': '',
    'Size': ''
}


def CallFun(cmd, Find):
    if cmd == 'Type':
        if Find['Type'] == 'Dog' or Find['Type'] == 'Cat':
            print('A Pet:')
        else:
            print('A Transport:')
    elif cmd == "Print":
        print(Find)
    else:
        print('error')


def GiveInfo(i):
    type0 = ['Dog', 'Cat']
    type1 = ['Car', 'Truck']
    color0 = ['Black', 'White', 'Pink']
    size0 = ['Big', 'Middle', 'Small']
    t0 = i % 2
    if t0 == 0:
        Find['Type'] = type0[i % 2]
    else:
        Find['Type'] = type1[i % 2]
    Find['Color'] = color0[i % 3]
    Find['Size'] = size0[i % 3]


def FindObj(num, cmd, CallBackFun):  # 发现目标，启动回调函数
    GiveInfo(num)  # 门卫填报信息
    CallBackFun(cmd, Find)  # 启动回调函数

if __name__ == '__main__':
    cmds = ['Type', 'Print', 'Try']
    for i in range(0, 10):  # 定义十次上报
        print('----------%d-------------' % i)
        FindObj(i, cmds[i % 3], CallFun)  # 这里注册回调函数（就是告知门卫的过程）
