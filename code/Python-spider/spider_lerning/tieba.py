# -*- coding:utf-8 -*-
import re
import urllib.request
import os
import sys


class TieBaPic:
    def __init__(self, page):
        self.siteUrl = 'http://tieba.baidu.com/p/3205263090?pn=' + str(page)
        self.page = page

    def get_html(self):
        response = urllib.request.urlopen(self.siteUrl)
        html = response.read().decode('UTF-8')
        # print(html)
        return html

    def get_img(self):
        pattern = r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
        img = re.compile(pattern)
        imglist = re.findall(img, self.get_html())
        imgCount = 0
        for image in imglist:
            # print(image + '\n')
            f = open(os.path.dirname(
                sys.argv[0]) + "/tie_pic/"+str(self.page)+'_'+str(imgCount) + '.jpg', "wb")
            f.write((urllib.request.urlopen(image)).read())
            print("正在下载【" + str(self.page) + '】页,第【' + str(imgCount) + '】条\n')
            f.close()
            imgCount += 1


if __name__ == "__main__":
    page = 1
    while page < 31:
        tiepic = TieBaPic(page)
        tiepic.get_img()
        page += 1
