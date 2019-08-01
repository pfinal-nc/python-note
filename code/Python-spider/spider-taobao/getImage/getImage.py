# -*- coding:utf-8 -*-
import time
import os
import requests
import xlrd
import xlwt
import config
import pymysql
import random
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import FirefoxOptions
from fake_useragent import UserAgent


def get_img(url, platform, id):
    proxies = [
        'http://58.218.214.198:4251',
        'http://58.218.214.139:9835',
        'http://58.218.92.157:2088',
        'http://58.218.92.154:9676',
        'http://58.218.214.162:5827',
        'http://58.218.214.158:6532',
        'http://58.218.92.169:3685',
    ]
    if Path(os.getcwd() + '/images/' + id).exists() == False:
        images = {}
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        opts.add_argument("--proxy-server=%s" % (random.sample(proxies, 1)[0]))
        # driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", firefox_options=opts)
        driver = webdriver.Firefox(executable_path="/home/pfinal/.pyenv/versions/3.7.3/geckodriver")
        driver.get(url)
        time.sleep(3)
        btn = driver.find_element_by_id('sufei-dialog-close')
        btn.click()
        images['goods_image'] = []
        if platform == u'天猫':
            # J_UlThumb > li:nth-child(2) > div > a > img
            list_img = driver.find_elements_by_css_selector('#J_UlThumb>li>a>img')
        else:
            list_img = driver.find_elements_by_css_selector('#J_UlThumb>li>div>a>img')
        # print(list_img)
        if len(list_img) > 0:
            for i in range(1, len(list_img) + 1):
                if platform == u'天猫':
                    img_selector = '#J_UlThumb > li:nth-child(%d)  > a > img' % i
                else:
                    img_selector = '#J_UlThumb > li:nth-child(%d)  > div > a > img' % i
                img = driver.find_elements_by_css_selector(img_selector)
                if len(img) > 0:
                    images['goods_image'].append(img[0].get_attribute('src'))
                # time.sleep(1)

        # driver.maximize_window()
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
                        setTimeout(f, 1000);
                    })();
                    """)
        WebDriverWait(driver, 50)
        # time.sleep(10)
        # print(images)
        images['goods_info_image'] = []
        if platform == u'天猫':
            goods_info_img = driver.find_elements_by_css_selector('#description > div > p > img')
            if len(goods_info_img) > 0:
                for j in range(1, len(goods_info_img) + 1):
                    goods_info_img_selector = "#description > div > p > img:nth-child(%d)" % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector)
                    if len(info_img) > 0:
                        images['goods_info_image'].append(info_img[0].get_attribute('src'))
            else:
                goods_info_img = driver.find_elements_by_css_selector('#description > div > p:nth-child(2) > img')
                if len(goods_info_img) > 0:
                    for j in range(1, len(goods_info_img) + 1):
                        goods_info_img_selector = "#description > div > p:nth-child(2) > img:nth-child(%d)" % j
                        info_img = driver.find_elements_by_css_selector(goods_info_img_selector)
                        if len(info_img) > 0:
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))

        else:
            goods_info_img = driver.find_elements_by_css_selector('#J_DivItemDesc > p:nth-child(1) > img')

            # # J_DivItemDesc > p > img:nth-child(1)
            if len(goods_info_img) > 0:
                # print(goods_info_img)
                for j in range(1, len(goods_info_img) + 1):
                    goods_info_img_selector = "#J_DivItemDesc > p:nth-child(1) > img:nth-child(%d)" % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector)
                    if len(info_img) > 0:
                        try:
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
                        except:
                            continue
            else:
                #     # J_DivItemDesc > p > img:nth-child(1)
                goods_info_img = driver.find_elements_by_css_selector('#J_DivItemDesc > p > img')
                # print(goods_info_img)
                for j in range(1, len(goods_info_img) + 1):
                    goods_info_img_selector = "#J_DivItemDesc > p > img:nth-child(%d)" % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector)
                    # print(info_img)
                    if len(info_img) > 0:
                        try:
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
                        except:
                            continue

        # with open(os.getcwd() + '/images.txt', "a+", encoding="utf-8") as f:
        # f.write(str(images) + '\n')
        # f.flush()
        # f.close()
        img_save(images, os.getcwd() + '/images/' + str(id), platform, url)
        # download_img(url)
        # db = pymysql.connect(config.HOST, config.USER, config.PASSWORD, config.DATABASE)
        # # 使用 cursor() 方法创建一个游标对象 cursor
        # cursor = db.cursor()
        # sql = "UPDATE shopnc_taobao_goods SET pic_spilder_status=1 WHERE t_id=" + id
        # try:
        #     cursor.execute(sql)
        #     db.commit()
        # except:
        #     db.rollback()
        # driver.close()


def img_save(images, file_path, platform, url):
    headers = {
        "Host": "img.alicdn.com",
        "User-Agent": UserAgent().random,
        "Referer": url
    }
    proxy_list = [
        {'http': '58.218.214.198:4251'},
        {'http': '58.218.214.139:9835'},
        {'http': '58.218.92.157:2088'},
        {'http': '58.218.92.154:9676'},
        {'http': '58.218.214.162:5827'},
        {'http': '58.218.214.158:6532'},
        {'http': '58.218.92.169:3685'}
    ]
    if len(images['goods_image']) > 0:
        i = 1
        for img in images['goods_image']:
            if platform == u'天猫':
                img_url = img.strip('.jpg').strip('60x60q90').strip('_')
            else:
                if img.find('50x50') > 0:
                    img_url = img.strip('.jpg').strip('50x50').strip('_')
                else:
                    img_url = img.strip('.jpg').strip('400x400').strip('_')
            # print(img_url)
            if img.find('gif') < 0:
                r = requests.get(img_url + '?time=' + str(time.time()), proxies=random.choice(proxy_list), timeout=30, headers=headers)
                # print(r)
                save_path = Path(str(file_path) + '/cover/')
                if save_path.exists() == False:
                    os.makedirs(save_path)
                with open(str(save_path) + '/%s.%s' % (str(i), img_url.split('.')[-1]), 'wb') as f:
                    f.write(r.content)
                i += 1
    if len(images['goods_info_image']) > 0:
        j = 1
        for img_info in images['goods_info_image']:
            res = requests.get(img_info + '?time=' + str(time.time()), timeout=30, headers=headers)
            # print()
            save_info_path = Path(str(file_path) + '/details/')
            if save_info_path.exists() == False:
                os.makedirs(save_info_path)
            with open(str(save_info_path) + '/%s.%s' % (str(j), img_info.split('.')[-1]), 'wb') as f:
                f.write(res.content)
            j += 1


def read_data():
    db = pymysql.connect(config.HOST, config.USER, config.PASSWORD, config.DATABASE)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "SELECT t_id,detail_url,system_type FROM shopnc_taobao_goods WHERE pic_spilder_status=0 AND system_type='天猫'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            wb = xlwt.Workbook(encoding='utf-8', style_compression=0)
            ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)
            k = 0
            for data in [u'商品ID', u'商品详情页', u'平台类型']:
                ws.write(0, k, data)
                k = k + 1
            j = 1
            for row in results:
                k = 0
                for row_content in row:
                    ws.write(j, k, str(row_content))
                    k = k + 1
                j = j + 1
                #     ws.write(0, k, str(row))
            save_name = os.getcwd() + '/excel/test.xls'
            wb.save(save_name)
    except:
        print("数据库链接失败")
    db.close()


def read_excel(excel_path):
    excel_data = []
    data = xlrd.open_workbook(excel_path)
    sheet0 = data.sheet_by_index(0)
    rows = sheet0.nrows  # 行总数
    i = 1
    while (i < rows):
        row_data = sheet0.row_values(i)
        excel_data.append({'id': row_data[0], 'url': row_data[1], 'platform': row_data[2]})
        i = i + 1
    return excel_data
