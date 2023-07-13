# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 09:17
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : tqdm_demo.py
# @Software: PyCharm
from time import sleep

from tqdm.notebook import tqdm

# tqdm 主要参数
# iterable: 可迭代的对象, 在手动更新时不需要进行设置
# desc: str, 左边进度条的描述性文字
# total: 总的项目数
# leave: bool, 执行完成后是否保留进度条
# file: 输出指向位置, 默认是终端, 一般不需要设置
# ncols: 调整进度条宽度, 默认是根据环境自动调节长度, 如果设置为0, 就没有进度条, 只有输出的信息
# unit: 描述处理项目的文字, 默认是'it', 例如: 100 it/s, 处理照片的话设置为'img' ,则为 100 img/s
# unit_scale: 自动根据国际标准进行项目处理速度单位的换算, 例如 100000 it/s >> 100k it/s
# colour: 进度条颜色，例如：'green', '#00ff00'。

if __name__ == '__main__':
    # for char in tqdm(['C', 'Python', 'PHP', 'Java', 'C++']):
    #     sleep(0.25)

    for i in tqdm(range(100)):
        sleep(0.05)
