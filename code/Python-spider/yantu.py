# -*- coding:utf-8 -*-

import threading
import requests
import random

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}

DIR_PATH = r"D:\素材\yan"
def get_img():
    url = 'https://yantuz.cn/mmPic/index.php?t=&v='+ str(random.random())
    # print(url)
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        print(response)
        img_name = DIR_PATH + "\pic_cnt_{}.jpg".format(random.random())
        with open(img_name, 'ab') as f:
            f.write(response.content)
            print(img_name)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    i = 110000
    while i >=0:
        get_img()
        i -=1

