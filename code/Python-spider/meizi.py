# -*- coding:utf-8 -*-
import re
import os
import time
import requests
from bs4 import BeautifulSoup
HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}

# 下载图片保存路径
DIR_PATH = r"D:\素材\mzitu"

def get_urls():
    page_urls = ['http://www.mzitu.com/page/{cnt}'.format(cnt=cnt) for cnt in range(1, 193)]
    print("Please wait for second ...")
    img_urls = []
    for page_url in page_urls:
        # print(page_url)
        try:
            bs = BeautifulSoup(requests.get(page_url,headers=HEADERS,timeout=10).text,'lxml').find('ul', id="pins")
            # print(bs)
            result = re.findall(r"(?<=href=)\S+", str(bs))  # 匹配所有 urls
            img_url = [url.replace('"', "") for url in result]
            img_urls.extend(img_url)
        except Exception as e:
            print(e)
    return set(img_urls)  # 利用 set 去重 urls

def urls_crawler(url):
    print(url)
    try:
        r = requests.get(url,headers=HEADERS,timeout=10).text
        folder_name = BeautifulSoup(r, 'lxml').find('div', class_="main-image").find('img')['alt'].replace("?", " ")
        if make_dir(folder_name):
            max_count = BeautifulSoup(r, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
            page_urls = [url + "/" + str(i) for i in range(1, int(max_count) + 1)]
            img_urls = []
            for _, page_url in enumerate(page_urls):
                time.sleep(0.25)
                result = requests.get(page_url, headers=HEADERS, timeout=10).text
                img_url = BeautifulSoup(result, 'lxml').find(
                    'div', class_="main-image").find(
                    'p').find('a').find('img')['src']
                img_urls.append(img_url)
            for cnt, url in enumerate(img_urls):
                save_pic(url, cnt)
    except Exception as e:
        print(e)

def save_pic(pic_src,pic_cnt):
    try:
        time.sleep(0.10)
        img = requests.get(pic_src, headers=HEADERS, timeout=10)
        img_name = "pic_cnt_{}.jpg".format(pic_cnt + 1)
        with open(img_name, 'ab') as f:
            f.write(img.content)
            print(img_name)
    except Exception as e:
        print(e)

def make_dir(folder_name):
    path = os.path.join(DIR_PATH, folder_name)
    # 如果目录已经存在就不用再次爬取了，去重，提高效率。存在返回 False，否则反之
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
        os.chdir(path)
        return True
    print("Folder has existed!")
    return False

if __name__ == '__main__':
    urls = get_urls()
    for url in urls:
        urls_crawler(url)
    #urls_crawler(urls)
