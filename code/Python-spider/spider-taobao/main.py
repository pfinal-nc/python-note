# -*- coding:utf-8 -*-
import os
import config
from getImage.getImage import get_img
from getImage.getImage import read_excel
from getImage.getImage import read_data
from getImage.getImage import get_check_data


def self_thread(data, thread_num):
    # print(data)
    print("开始爬取：" + str(thread_num))
    if len(data) > 0:
        for i in data:
            get_img(i[1], i[2], i[0])


if __name__ == '__main__':
    # goods_list = read_data()
    goods_list = get_check_data()
    print(goods_list)
    # print(goods_list)
    # for i in goods_list:
    #     get_img(i[1], i[2], i[0])
    # excel_path = os.getcwd() + '/excel/test.xls'
    # data_list = read_excel(excel_path)
    # thread_list = []
    if len(goods_list) > 50:
        thread_data = [goods_list[i:i + 50] for i in range(0, len(goods_list), 10)]
        # print(thread_data)
        j = 1
        for i in thread_data:
            self_thread(i, j)
    else:
        self_thread(goods_list, 1)
