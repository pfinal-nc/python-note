# -*- coding: utf-8 -*-
# @Time    : 2023/8/8 10:54
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 获取.py
# @Software: PyCharm
import time

import execjs
from LunarSolarConverter.LunarSolarConverter import LunarSolarConverter, Solar

with open('get_lun.js', 'r', encoding="utf-8") as f:
    get_lun_js = f.read()


def get_info(date, to):
    """Run the specified"""

    get_lun = execjs.compile(get_lun_js)
    result = get_lun.call('get_lun', date, int(to))
    print(result)


def fortunetelling(cday):
    """fortunetelling the specified"""
    # 农历 月 日 时，数字形态
    year = int(time.strftime("%Y", cday))
    month = int(time.strftime("%m", cday))
    day = int(time.strftime("%d", cday))
    hour = int(time.strftime("%H", cday))
    print("当前时间: " + str(year) + "年" + str(month) + "月" + str(day) + "日 " + str(hour) + "时")
    hour = ((hour + 1) / 2 + 1) % 12

    converter = LunarSolarConverter()
    solar = Solar(year, month, day)
    lunar = converter.SolarToLunar(solar)

    # 小六壬对应的位置
    liuren_month = lunar.lunarMonth % 6
    liuren_day = (lunar.lunarMonth + lunar.lunarDay - 1) % 6
    liuren_hour = (lunar.lunarMonth + lunar.lunarDay + hour - 2) % 6

    if liuren_month == 1:
        print("农历" + str(lunar.lunarMonth) + "月 -- " + "大安月")
    elif liuren_month == 2:
        print("农历" + str(lunar.lunarMonth) + "月 -- " + "留连月")
    elif liuren_month == 3:
        print("农历" + str(lunar.lunarMonth) + "月 -- " + "速喜月")
    elif liuren_month == 4:
        print("农历" + str(lunar.lunarMonth) + "月 -- ""赤口月")
    elif liuren_month == 5:
        print("农历" + str(lunar.lunarMonth) + "月 -- ""小吉月")
    elif liuren_month == 0:
        print("农历" + str(lunar.lunarMonth) + "月 -- ""空亡月")
    if liuren_day == 1:
        print(
            "农历" + str(lunar.lunarDay) + "日 -- " + "大安日")
    elif liuren_day == 2:
        print(
            "农历" + str(lunar.lunarDay) + "日 -- " + "留连日")
    elif liuren_day == 3:
        print(
            "农历" + str(lunar.lunarDay) + "日 -- " + "速喜日")
    elif liuren_day == 4:
        print(
            "农历" + str(lunar.lunarDay) + "日 -- ""赤口日")
    elif liuren_day == 5:
        print(
            "农历" + str(lunar.lunarDay) + "日 -- ""小吉日")
    elif liuren_day == 0:
        print("农历" + str(lunar.lunarDay) + "日 -- ""空亡日")
    if hour == 1:
        lunarHour = "子"
    elif hour == 2:
        lunarHour = "丑"
    elif hour == 3:
        lunarHour = "寅"
    elif hour == 4:
        lunarHour = "卯"
    elif hour == 5:
        lunarHour = "辰"
    elif hour == 6:
        lunarHour = "巳"
    elif hour == 7:
        lunarHour = "午"
    elif hour == 8:
        lunarHour = "未"
    elif hour == 9:
        lunarHour = "申"
    elif hour == 10:
        lunarHour = "酉"
    elif hour == 11:
        lunarHour = "戌"
    elif hour == 12:
        lunarHour = "亥"
    if liuren_hour == 1:
        print("农历" + lunarHour + "时 -- " + "大安时")
        print("大安事事昌，求财在坤方，失物去不远，宅舍保安康\n行人身未动，病者主无妨，将军回田野，仔细更推详")
    elif liuren_hour == 2:
        print("农历" + lunarHour + "时 -- " + "留连时")
        print("留连事难成，求谋日未明，官事凡宜缓，去者未回程\n失物南方见，急讨方心称，更须防口舌，人口且平平")
    elif liuren_hour == 3:
        print("农历" + lunarHour + "时 -- " + "速喜时")
        print("速喜喜来临，求财向南行，失物申未午，逢人路上寻\n官事有福德，病者无祸侵，田宅六畜吉，行人有信音")
    elif liuren_hour == 4:
        print("农历" + lunarHour + "时 -- ""赤口时")
        print("赤口主口舌，官非切宜防，失物速速讨，行人有惊慌\n六畜多作怪，病者出西方，更须防咀咒，诚恐染瘟皇")
    elif liuren_hour == 5:
        print("农历" + lunarHour + "时 -- ""小吉时")
        print("小吉最吉昌，路上好商量，阴人来报喜，失物在坤方\n行人即便至，交关甚是强，凡事皆和合，病者叩穷苍")
    elif liuren_hour == 0:
        print("农历" + lunarHour + "时 -- ""空亡时")
        print("空亡事不祥，阴人多乖张，求财无利益，行人有灾殃\n失物寻一见，官事有刑伤，病人逢暗鬼，解禳保安康")


if __name__ == '__main__':
    action = input('请输入1 查询八字,2 小六壬:')
    if action == "1":
        date = input('请输入要查询的日期:')
        to = input('请输入农历或者阳历:')
        get_info(date, to)
    else:
        a = input('请输入日期，格式为yyyy-mm-dd hour，使用当前时间，请直接回车 \n')
        if a == '':
            cday = time.localtime()
        else:
            cday = time.strptime(a, '%Y-%m-%d %H')
        fortunetelling(cday)
