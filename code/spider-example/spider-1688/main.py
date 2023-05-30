# -*- coding: utf-8 -*-
import os
import threading
import multiprocessing as mp
import queue
from spider import Spider


def run(data, mp_name):
    print('开始进程:【' + mp_name + "】")
    # print(data)
    Spider.Spider(excel_path).get_image(data)


if __name__ == '__main__':
    # str = 'https://cbu01.alicdn.com/img/ibank/2019/827/611/11050116728_1605606987.60x60.jpg_.webp'
    # print(str.strip('_.webp').strip('.jpg').strip('60x60') + 'jpg')
    excel_path = os.getcwd() + '/excel/'
    if len(os.listdir(excel_path)) <= 0:
        quit('请放入商品列表')
    else:
        spider_data = Spider.Spider(excel_path).url_data
        excel_list = [spider_data[i:i + 5] for i in range(0, len(spider_data), 5)]
        mp_list = []
        for i in range(0, len(excel_list)):
            mp_name = mp.Process(target=run, args=(excel_list[i], 'mp_name_' + str(i)))
            mp_list.append(mp_name)
        if len(mp_list) > 0:
            for item in mp_list:
                item.start()
            for item_stop in mp_list:
                item_stop.join()

    Spider.Spider(excel_path).rar_file('./images',os.getcwd() + '/')

