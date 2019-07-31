# -*- coding:utf-8 -*-
import os
import threading
import time
from pathlib import Path
from getImage.getImage import get_img
from getImage.getImage import read_excel
from getImage.getImage import read_data
from fake_useragent import UserAgent


def self_thread(data, thread_num):
    # print(data)
    print("开始线程：" + str(thread_num))
    if len(data) > 0:
        for i in data:
            time.sleep(2)
            # print(type(i['id']))
            get_img(i['url'], i['platform'], i['id'])
            # download_img(i['url'])
    # print("退出线程：" + self.threadID)


if __name__ == '__main__':
    # read_data()
    # # 读取excel
    excel_path = os.getcwd() + '/excel/test.xls'
    data_list = read_excel(excel_path)
    thread_list = []
    if len(data_list) > 10:
        thread_data = [data_list[i:i + 10] for i in range(0, len(data_list), 10)]
        j = 1
        for i in thread_data:
            t1 = threading.Thread(target=self_thread, args=(i, j))
            thread_list.append(threading.Thread(target=self_thread, args=(i, j)))
            j += 1
        # print()
        if len(thread_list) > 0:
            for k in thread_list:
                k.start()
                k.join()
    else:
        # selfThread('1', data_list).start()
        threading.Thread(target=self_thread, args=(data_list, 1)).start()
