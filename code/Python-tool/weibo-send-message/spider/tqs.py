import json
import random
import os
import xlrd
from weibo.weibo_message import WeiboMessage


class TqsParse():

    def __init__(self):
        super(TqsParse, self)

    def download_text(self):
        excel = os.getcwd() + '/excel/2020-03-02_导出优惠券.xls'
        #print(excel)
        workbook = xlrd.open_workbook(excel)
        # 选取需要读取数据的那一页
        sheet = workbook.sheet_by_index(0)
        # 获得行数和列数
        rows = sheet.nrows

        p = []
        for i in range(1, rows):
           values = sheet.row_values(i)
           p.append({
               'name':values[1],
               'z_img':values[5],
               'payment':values[17],
               'tk_link':values[20]
           })
        return json.dumps(p,ensure_ascii=False)

    def get_weibo_message(self):
        msg=''
        json_text = self.download_text()
        #print(json_text)
        items = self.getItems(json_text)
        #print(items)
        count = len(items)
        # print(count)
        if count > 0:
            index = random.randint(0, count - 1)
            msg = items[index]
        return WeiboMessage(msg["text"],msg["images"])
    
    def getItems(self, jsonStr):
        items = []
        nodes = json.loads(jsonStr)
        #print(nodes)
        for node in nodes: 
            # print(node)
            msg = '[给力] '+ node["name"] + ' [赞啊] 券后价: 【'+ str(node['payment']) +'】 [赞啊]【优惠券领取】'
            url = node["tk_link"]
            item = "%s %s" % (msg, url)
            items.append({"text":item,"images":[node["z_img"],"https://wx4.sinaimg.cn/mw1024/9db4902dgy1g43wz7ua2aj20br0ekq51.jpg",node["z_img"]]})
        return items