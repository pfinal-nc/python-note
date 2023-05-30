# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 17:21
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : open.py
# @Software: PyCharm

# Api = https://learn.open.com.cn/Account/UnitLogin?bust=1683624055001
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://learn.open.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://learn.open.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}

# 参数:
# loginName: 111111111
# passWord: 213qwe
# validateNum:
# black_box: qWPSl1683623991xb5N7xcNUu4