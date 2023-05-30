# -*- coding:utf-8 -*-
import os
import threading
import time
from pathlib import Path
from getImage.getImage import get_img
from getImage.getImage import read_excel
from getImage.getImage import read_data
from fake_useragent import UserAgent
import multiprocessing as mp
import threading as td


def self_thread(q, data, thread_num):
    # print(data)
    print("开始爬取：" + str(thread_num))
    print(data)
    for i in data:
        # print(i['url'].split("=", 1)[1])
        # print(i['platform'])
        get_img(i['url'], i['platform'], i['url'].split("=", 1)[1])

    q.put("爬取：" + str(thread_num))


if __name__ == '__main__':
    # goods_list = read_data()
    goods_list = read_excel('./taobao.xlsx')
    # print(goods_list)
    q = mp.Queue()
    if len(goods_list) > 50:
        thread_data = [goods_list[i:i + 50] for i in range(0, len(goods_list), 50)]
        # print(thread_data)
        j = 1
        p = []

        for i in thread_data:
            p.append(mp.Process(target=self_thread, args=(q, i, j)))
            # self_thread(i, j)
            j += 1
        for item in p:
            item.start()
        for item in p:
            item.join()

    else:
        self_thread(q, goods_list, 1)
