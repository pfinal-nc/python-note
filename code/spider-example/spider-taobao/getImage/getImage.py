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
from selenium.webdriver import FirefoxOptions
from fake_useragent import UserAgent


def get_img(url, platform, id):
      proxies = config.PROXIES
      if Path(os.getcwd() + '/images/' + id).exists() == False:
        images = {}
        opts = FirefoxOptions()
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        profile = FirefoxProfile()
        proxies_on = random.choice(proxies).split(':')
        profile.set_preference("network.proxy.http", proxies_on[0])
        profile.set_preference("network.proxy.http_port", proxies_on[1])
        #driver = webdriver.Firefox(profile, options=options, executable_path="/usr/local/bin/geckodriver")
        #driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")
        driver = webdriver.Firefox(executable_path="/home/pfinal/.pyenv/versions/3.7.3/geckodriver")
        driver.get(url)
        time.sleep(1)
        try:
            btn = driver.find_element_by_id('sufei-dialog-close')
            btn.click()
        except:
            pass

        images['goods_image'] = []
        if platform == u'天猫':
            # J_UlThumb > li:nth-child(2) > div > a > img
            list_img = driver.find_elements_by_css_selector('#J_UlThumb>li>a>img')
            if len(list_img) <=0:
               list_img = driver.find_elements_by_css_selector('#J_UlThumb>li')
        else:
            list_img = driver.find_elements_by_css_selector('#J_UlThumb>li>div>a>img')
        # print(list_img)
        if len(list_img) >0:

            for i in range(1, len(list_img) + 1):
                img_selector = '#J_UlThumb > li:nth-child(%d)  > a > img' % i
                #J_UlThumb > li:nth-child(2) > a > img

                img = driver.find_elements_by_css_selector(img_selector)
               
                if len(img) > 0:
                   images['goods_image'].append(img[0].get_attribute('src'))
                
                img_selector_2 = '#J_UlThumb > li:nth-child(%d)>div > a > img' % i
                
                img_2 = driver.find_elements_by_css_selector(img_selector_2)
                if len(img_2) > 0:
                   images['goods_image'].append(img[0].get_attribute('src'))
                time.sleep(1)

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
        time.sleep(30)
        # driver.switch_to_alert().accept()
        # print(images)
        if platform == u'天猫':
            images['goods_info_image'] = []
            goods_info_img_a = driver.find_elements_by_css_selector('#description > div > p > img')
            if len(goods_info_img_a) > 0:
                for j in range(1, len(goods_info_img_a) + 1):
                    goods_info_img_selector_a = "#description > div > p > img:nth-child(%d)" % j
                    info_img_a = driver.find_elements_by_css_selector(goods_info_img_selector_a)
                    if len(info_img_a) > 0:
                       # images['goods_info_image'] = []
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
        driver.close()
        # download_img(url)
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
                r = requests.get(img_url,proxies=random.choice(proxy_list),timeout=30, headers=headers)
                #r = requests.get(img_url,timeout=30, headers=headers)
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
            # time.sleep(1)
            res = requests.get(img_info,proxies=random.choice(proxy_list), timeout=30, headers=headers)
            # res = requests.get(img_info, timeout=30, headers=headers)
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
    sql = "SELECT t_id,detail_url,system_type FROM shopnc_taobao_goods WHERE pic_spilder_status=0 AND state=1 AND is_true=0"
    #sql = "SELECT t_id,detail_url,system_type FROM shopnc_taobao_goods WHERE t_id in ('588389986388','596855134938','594629210954','589919558541','587916026378','597202860027','594980790612','521371248226','554924023146','575045049032','596450223037','564512163455','595734421421','587293937506','592188413004','587128468015','595968613298','568958219328','557519682967','586792542010','596868930960','577461216715','587050860545','589533330549','548516889786','594979674254','597283702668','584446103694','592692323396','594004146928','599361041823','561040695579','589025714967','549919835560','22665244361','589512829959','564951402607','597631708917','595645956270','10688781658','583099954491','577747848489','594818349296','586635409205','590933771226','598129269695','592500668483','587314792709','593034162171','571217802686','540999214510','575371569469','597578848466','587382480318','596453520212','598957137089','578139552715','588207255218','565465198872','577181759415','589471793817','581198751584','573104892589','595090591537','594570941584','558505312109','598373996931','589690023598','575686356924','568121248176','586368085894','558147548102')";
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
        #excel_data.append({'id': row_data[0], 'url': row_data[1], 'platform': row_data[2]})
        excel_data.append({'id': row_data[0], 'url': row_data[5], 'platform': row_data[4]})
        i = i + 1
    return excel_data
