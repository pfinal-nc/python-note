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
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.proxy import Proxy, ProxyType
from fake_useragent import UserAgent


def get_img(url, platform, id):
    if Path(os.getcwd() + '/images/' + id).exists() == False:
        proxies = config.PROXIES
        images = {}
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        profile = FirefoxProfile()
        proxies_on = random.choice(proxies).split(':')
        profile.set_preference("network.proxy.http", proxies_on[0])
        profile.set_preference("network.proxy.http_port", proxies_on[1])
        # driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", firefox_options=opts)
        driver = webdriver.Firefox(profile, options=options,
                                   executable_path="/home/pfinal/.pyenv/versions/3.7.3/geckodriver")
        driver.get(url)
        time.sleep(3)
        try:
            btn = driver.find_element_by_id('sufei-dialog-close')
            btn.click()
        except:
            pass
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
                        setTimeout(f, 1500);
                    })();
                    """)
        WebDriverWait(driver, 50)
        # print(images)
        images['goods_info_image'] = []
        time.sleep(20)

        if platform == u'天猫':
            goods_info_img_a = driver.find_elements_by_css_selector('#description > div > p > img')
            if len(goods_info_img_a) > 0:
                for j in range(1, len(goods_info_img_a) + 1):
                    goods_info_img_selector_a = "#description > div > p > img:nth-child(%d)" % j
                    info_img_a = driver.find_elements_by_css_selector(goods_info_img_selector_a)
                    if len(info_img_a) > 0:
                        if info_img_a[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img_a[0].get_attribute('src'))

            goods_info_img_b = driver.find_elements_by_css_selector('#description > div > p:nth-child(2) > img')
            if len(goods_info_img_b) > 0:
                for j in range(1, len(goods_info_img_b) + 1):
                    goods_info_img_selector_b = "#description > div > p:nth-child(2) > img:nth-child(%d)" % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_b)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
                    # description > div > div:nth-child(6) > div:nth-child(1) > img
            goods_info_img_c = driver.find_elements_by_css_selector('#description > div > div:nth-child(6) > div')

            if len(goods_info_img_c) > 0:
                for j in range(1, len(goods_info_img_c) + 1):
                    goods_info_img_selector_c = '#description > div > div:nth-child(6) > div:nth-child(%d) > img' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_c)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))

            goods_info_img_d = driver.find_elements_by_css_selector(
                '#description > div > table:nth-child(4) > tbody > tr > td > p:nth-child(3) > img')
            if len(goods_info_img_d) > 0:
                for j in range(1, len(goods_info_img_d) + 1):
                    goods_info_img_selector_d = '#description > div > table:nth-child(4) > tbody > tr > td > p:nth-child(3) > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_d)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))

            goods_info_img_e = driver.find_elements_by_css_selector("#description > div > div > div > img")
            if len(goods_info_img_e) > 0:
                for j in range(1, len(goods_info_img_e) + 1):
                    goods_info_img_selector_e = '#description > div > div > div > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_e)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
            # description > div > p:nth-child(5) > a:nth-child(2) > img
            goods_info_img_f = driver.find_elements_by_css_selector(
                "#description > div > p:nth-child(5) > a:nth-child(2) > img")
            if len(goods_info_img_f) > 0:
                for j in range(1, len(goods_info_img_f) + 1):
                    goods_info_img_selector_f = '#description > div > p:nth-child(5) > a:nth-child(2) > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_f)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))

            goods_info_img_g = driver.find_elements_by_css_selector("#description > div > img")
            if len(goods_info_img_g) > 0:
                for j in range(1, len(goods_info_img_g) + 1):
                    goods_info_img_selector_g = '#description > div > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_g)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
            goods_info_img_h = driver.find_elements_by_css_selector(
                '#description > div > table > tbody > tr > td > div > table > tbody > tr > td > p > img')
            if len(goods_info_img_h) > 0:
                for j in range(1, len(goods_info_img_h) + 1):
                    goods_info_img_selector_h = '#description > div > table > tbody > tr > td > div > table > tbody > tr > td > p > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_h)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
            goods_info_img_o = driver.find_elements_by_css_selector("#description > div > div > img")
            if len(goods_info_img_o) > 0:
                for j in range(1, len(goods_info_img_o) + 1):
                    goods_info_img_selector_o = '#description > div > div > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_o)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
            goods_info_img_p = driver.find_elements_by_css_selector("#description > div > div:nth-child(6) > img")
            if len(goods_info_img_p) > 0:
                for j in range(1, len(goods_info_img_p) + 1):
                    goods_info_img_selector_p = '#description > div > div:nth-child(6) > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_p)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
            goods_info_img_q = driver.find_elements_by_css_selector("#description > div > p > a > img")
            if len(goods_info_img_q) > 0:
                for j in range(1, len(goods_info_img_q) + 1):
                    goods_info_img_selector_q = '#description > div > p > a > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_q)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))
            goods_info_img_r = driver.find_elements_by_css_selector(
                '#description > div > table > tbody > tr > td > img')
            if len(goods_info_img_r) > 0:
                for j in range(1, len(goods_info_img_r) + 1):
                    goods_info_img_selector_r = '#description > div > table > tbody > tr > td > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_r)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))

            goods_info_img_s = driver.find_elements_by_css_selector("#description > div > p > span > img")
            if len(goods_info_img_s) > 0:
                for j in range(1, len(goods_info_img_s) + 1):
                    goods_info_img_selector_s = '#description > div > p > span > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_s)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))

            goods_info_img_t = driver.find_elements_by_css_selector("#description > div > p:nth-child(4) > b > img")
            if len(goods_info_img_t) > 0:
                for j in range(1, len(goods_info_img_t) + 1):
                    goods_info_img_selector_t = '#description > div > p:nth-child(4) > b > img:nth-child(%d)' % j
                    info_img = driver.find_elements_by_css_selector(goods_info_img_selector_t)
                    # print(info_img)
                    if len(info_img) > 0:
                        if info_img[0].get_attribute('src') != 'https://img-tmdetail.alicdn.com/tps/i3/T1BYd_XwFcXXb9RTPq-90-90.png':
                            images['goods_info_image'].append(info_img[0].get_attribute('src'))


        else:
            goods_info_img = driver.find_elements_by_css_selector('#J_DivItemDesc > p:nth-child(1) > img')

            # description > div > p > span > img:nth-child(1)
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

        with open(os.getcwd() + '/images.txt', "a+", encoding="utf-8") as f:
            f.write(str(images) + '\n')
            f.flush()
            f.close()
        # print(images)
        img_save(images, os.getcwd() + '/images/' + str(id), platform, url)

        driver.close()
        db = pymysql.connect(config.HOST, config.USER, config.PASSWORD, config.DATABASE)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "UPDATE shopnc_taobao_goods SET pic_spilder_status=1 WHERE t_id=" + id
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()


def img_save(images, file_path, platform, url):
    headers = {
        "Host": "img.alicdn.com",
        "User-Agent": UserAgent().random,
        "Referer": url
    }
    proxy_list = []
    for ip in config.PROXIES:
        proxy_list.append({"http": ip})
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
                r = requests.get(img_url, proxies=random.choice(proxy_list), timeout=30,
                                 headers=headers)
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
            res = requests.get(img_info, timeout=30, headers=headers)
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
    sql = "SELECT t_id,detail_url,system_type FROM shopnc_taobao_goods WHERE pic_spilder_status=0 AND is_true=0"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            return results
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


def get_check_data():
    db = pymysql.connect(config.HOST, config.USER, config.PASSWORD, config.DATABASE)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "SELECT t_id,detail_url,system_type FROM shopnc_taobao_goods WHERE t_id in (590048337967,38851585942,586147361240,595829102487,561645942309,591135184586,593999592596,596441448615,580859291843,594372720673,559680679226,586637417218,591187957482,596333250363,45025095461,572606728136,595276672394,573697669961,577268623037,577380472169,578442483712,557103683985,571150105105,542154902166,586831593594,594531010602,576029597795,598788907192,565087426943,599950683814,586700874661,16037458686,594583936657,563375779813,576837129539,585692870393,598075362886,565125630796,578675934329,582297134201,578865342527,581789930748,574570146864,596732345012,595050603929,581006521282,588163572388,568750839115,588133210548,542775668767,592573568864,594585770921,581953229642,597448046490,38625749105,16733914490,587160931525,596761494808,531565017588,594196534171,589056748233,598102450043,559060544796,578892160859,588000554902,587584692337,37030139660,560884903648,567871669632,559735569960,589551495494,575067356395,594211327185,592734113980,554185014044,531448065506,534185159535,592483677514,591873489988,570982149821,596384253437,569519492636,547746378793,595707136959,545851391176,527995958675,585177340014,556580723906,571523044618,599055552702,567853690566,587886004915,591151962458,569562255453,575302314618,17511921527,584793406199,578715455186,571989517009,579792848912,595241887456,581912841082,541466029805,592710305041,580442138828,586935949433,576324490062,580042384358,592713194485,557007382944,577845459745,582166328701,596442575453,597737162481,21912167033,553756836914,36813723445,572237466961,555182235878,597641987237,590926517858,591028736907,592834389565,532884225550,594001913195,594728897094,585539127147,596047559885,563924192835,520777524076,570119157701,597612652873,586071477116,556923025304,599130082085,589138641777,590457440281,588951772934,592349531153,591398396284,578031385514,525809760523,596634933573,592107993219,41702352376,598099096010,586684920100,593950082754,588366166680,2251723664,585744254162,593705507236,591773694189,45725574278,548981528170,594226892993,576988212657,576706883047,532191001787,586670312456,567465860080,19088005402,520912495239,586632046322,565995815460,596296234625,577181759415,588570129124,45548585096,13490312444,549294129913,582681674613,551110223115,591830316342,533842012423,567587165474,578271443667,539547640594,592775860554,558188273335,578840009419,577183384111,26056724937,588174838051,593953392827,596631314796,550584648278,595502622668,35037274410,587315501405,559331315718,595197273191,528183278394,551930622853,524357542775,534086614552,591818920414,597084595937,557872793663)"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            return results
    except:
        print("数据库链接失败")
    db.close()
