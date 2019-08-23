# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pfinal'
__mtime__ = '2019/8/22'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                ┃┫┫  ┃┫┫
                ┗┻┛  ┗┻┛
"""
import config
import random
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.proxy import Proxy, ProxyType

DEBUG = False


def login():
    url = config.TB_URL
    print(url)
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(executable_path=config.GECKODRIVER_PATH)
    driver.get(url)
    driver.maximize_window()
    # J_Static2Quick
    time.sleep(5)
    # while True:
    frame = driver.find_element_by_xpath(
        '//*[@id="mx_n_19"]/div/iframe[contains(@src,"//login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true&disableQuickLogin=true")]')
    driver.switch_to.frame(frame)
    # 获取select标签

    select = driver.find_element_by_xpath('//*[@id="J_LoginBox"]/div[1]/div[1]/i[2]')
    select.click()
    time.sleep(random.uniform(0.5, 2))
    _input_simulation(driver.find_element_by_id('TPL_username_1'), '')
    time.sleep(random.uniform(0.5, 2))
    # browser.find_element_by_id('TPL_password_1').send_keys('abcdefgh')
    _input_simulation(driver.find_element_by_id('TPL_password_1'), '')
    driver.execute_script('Object.defineProperties(navigator,{webdriver:{get:()=>false}})')
    if _has_move(driver):
        print(u'有滑动验证 ================ ')
        _move_simulation(driver, driver.find_element_by_id('nc_1_n1z'))

    time.sleep(2)
    driver.find_element_by_id('J_SubmitStatic').submit()
    print(driver.get_cookies())
    newwindow = 'window.open("https://pub.alimama.com/myunion.htm")'
    driver.execute_script(newwindow)
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(2)
    driver.switch_to_window(driver.window_handles[0])
    #driver.switch_to_window(driver.window_handles[0])
    # if _error(driver):
    #     print(u'验证出错，刷新页面重试')
    #     driver.refresh()
    #     time.sleep(10)
    # time.sleep(2)


def _input_simulation(e, text):
    for i in range(len(text)):
        sleep_time = random.randint(8, 30)
        time.sleep(sleep_time / 10)
        e.send_keys(text[i])


def _has_move(driver):
    yanzhen = driver.find_element_by_id('nocaptcha')
    # print(yanzhen)
    style = yanzhen.get_attribute('style')
    # print(style)
    if style == 'display: block;':
        return True
    return False


def _move_simulation(device, e):
    try:
        action = ActionChains(device)
        action.click_and_hold(e).perform()
        # action.reset_actions()
        offset = 70
        for i in range(int(210 / offset)):
            ActionChains(device).move_by_offset(xoffset=offset, yoffset=0).perform()
            # time.sleep((offset - i) / 50)
        action.release().perform()
        action.reset_actions()
    except Exception as e:
        if DEBUG:
            print(e)


def _error(device):
    try:
        e = device.find_element_by_xpath('//*[@id="nocaptcha"]/div/span/a')
        if e:
            return True
        else:
            return False
    except Exception as e:
        if DEBUG: print(e)
        return True
