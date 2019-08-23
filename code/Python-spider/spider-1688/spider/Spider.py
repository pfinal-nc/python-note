# -*- coding: utf-8 -*-
import os
import xlrd
import time
import config
import requests
import zipfile
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.proxy import Proxy, ProxyType
from fake_useragent import UserAgent


class Spider(object):
    def __init__(self, excel_path):
        self.excel_path = excel_path
        self.init_read()

    def init_read(self):
        file_list = os.listdir(self.excel_path)
        file_path = self.excel_path + file_list[0]
        self.url_data = self.read_data(file_path)
        # self.get_image()

    # 读取excel 函数
    def read_data(self, file_path):
        excel_data = []
        data = xlrd.open_workbook(file_path)
        sheet0 = data.sheet_by_index(2)
        rows = sheet0.nrows  # 行总数
        i = 1
        while (i < rows):
            row_data = sheet0.row_values(i)
            # print(row_data)
            excel_data.append({'厂家': row_data[1], 'url': row_data[2]})
            i = i + 1
        return excel_data

    def get_image(self, url_data):
        if len(url_data) > 0:
            for url in url_data:
                self.save_img(url)
                time.sleep(5)
        else:
            exit()

    def save_img(self, url):
        print('开始抓取:【' + url['厂家'] + '】')
        self.image_cover = []
        self.image_detail = []
        if Path(os.getcwd() + '/images/').exists() == False:
            os.makedirs(os.getcwd() + '/images/')
        if Path(os.getcwd() + '/images/' + url['厂家']).exists() == False:
            options = webdriver.FirefoxOptions()
            options.add_argument('-headless')
            driver = webdriver.Firefox(options=options, executable_path=config.GECKODRIVER_PATH)
            driver.get(url['url'])
            driver.execute_script("""
                                (function () {
                                    var y = document.body.scrollTop;
                                    var step = 100;
                                    window.scroll(0, y);
                                    function f() {
                                        if (y < document.body.scrollHeight) {
                                            y += step;
                                            window.scroll(0, y);
                                            setTimeout(f, 50);
                                        }
                                        else {
                                            window.scroll(0, y);
                                            document.title += "scroll-done";
                                        }
                                    }
                                    setTimeout(f, 1500);
                                })();
                                """)
            time.sleep(10)
            try:
                btn = driver.find_element_by_id('sufei-dialog-close')
                btn.click()
            except:
                pass
            # dt-tab > div > ul > li:nth-child(1) > div > a > img

            self.get_image_cover(driver)
            self.get_image_detail(driver)
            self.img_save(os.getcwd() + '/images/' + url['厂家'], url)
            driver.close()

    def get_image_cover(self, driver):
        list_img = driver.find_elements_by_css_selector('#dt-tab > div > ul > li')
        if len(list_img) > 0:
            for i in range(1, len(list_img) + 1):
                img = driver.find_elements_by_css_selector(
                    "#dt-tab > div > ul > li:nth-child(%d) > div > a > img" % i)
                if len(img) > 0:
                    self.image_cover.append(img[0].get_attribute('src'))

    def get_image_detail(self, driver):
        image_selectors = [
            {'select': '#desc-lazyload-container > p:nth-child(9) > span > img', "nth": True},
            {'select': '#desc-lazyload-container > p:nth-child(7) > img', "nth": True},
            {'select': '#desc-lazyload-container > p:nth-child(8) > img', "nth": True},
            {'select': '#desc-lazyload-container > p > img', "nth": True},
            {'select': '#desc-lazyload-container > p:nth-child(14) > span > img', "nth": True},
        ]
        for selector in image_selectors:
            goods_info_img = driver.find_elements_by_css_selector(selector['select'])
            if len(goods_info_img) > 0:
                for j in range(1, len(goods_info_img) + 1):
                    if selector['nth'] == True:
                        goods_info_img_selector = selector['select'] + ':nth-child(%d)' % j
                        info_img = driver.find_elements_by_css_selector(goods_info_img_selector)
                        if len(info_img) > 0:
                            self.image_detail.append(info_img[0].get_attribute('src'))

            else:
                continue
        #

    def img_save(self, path, url):
        headers = {
            "Host": "cbu01.alicdn.com",
            "User-Agent": UserAgent().random,
            "Referer": url['url']
        }
        if len(self.image_cover) > 0:
            i = 1
            for img in self.image_cover:
                img_url = img.strip('_.webp').strip('.jpg').strip('60x60') + 'jpg'
                print('爬去封面第%d张' % i)
                r = requests.get(img_url, timeout=30, headers=headers)
                if r.status_code == 200:
                    save_path = Path(path + '/cover/')
                    if save_path.exists() == False:
                        os.makedirs(save_path)
                    with open(str(save_path) + '/%s.%s' % (str(i), img_url.split('.')[-1]), 'wb') as f:
                        f.write(r.content)
                    i += 1

        if len(self.image_detail) > 0:
            j = 1
            for img in self.image_detail:
                print('爬去详情第%d张' % i)
                r = requests.get(img, timeout=30, headers=headers)
                if r.status_code == 200:
                    save_path = Path(path + '/detail/')
                    if save_path.exists() == False:
                        os.makedirs(save_path)
                    with open(str(save_path) + '/%s.%s' % (str(j), img.split('.')[-1]), 'wb') as f:
                        f.write(r.content)
                    j += 1

    def rar_file(self, file_path, file_rar_path):
        f = zipfile.ZipFile(file_rar_path + '/images.zip', 'w',zipfile.ZIP_DEFLATED)
        result = self.get_zip_file(file_path, [])
        for file in result:
            f.write(file)
        f.close()

    def get_zip_file(self, file_path, result):
        files = os.listdir(file_path)
        for file in files:
            if os.path.isdir(file_path + '/' + file):
                self.get_zip_file(file_path + '/' + file, result)
            else:
                result.append(file_path + '/' + file)
        return result
