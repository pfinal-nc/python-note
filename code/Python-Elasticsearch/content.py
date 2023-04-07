# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 15:43
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : content.py
# @Software: PyCharm
from elasticsearch7 import Elasticsearch


class EsAction:
    def __init__(self):
        self.es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200}], timeout=3600)

    def InsertData(self):
        self.es.create(index="my_index", doc_type="test_type", id=11, ignore=[400, 409],
                       body={"name": "python", "addr": '四川省'})
        # 查询结果
        result = self.es.get(index="my_index", doc_type="test_type", id=11)
        print('单条数据插入完成：\n', result)

    def AddData(self):
        datas = [{
            'name': '美国留给伊拉克的是个烂摊子',
            'addr': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'
        }, {
            "name": "python",
            "addr": '四川省'
        }]
        for i, data in enumerate(datas):
            self.es.create(index="my_index", doc_type="test_type",
                           id=i, ignore=[400, 409], body=data)
        # 查询结果
        result = self.es.get(index="my_index", doc_type="test_type", id=0)
        print('\n批量插入数据完成：\n', result['_source'])

    def UpdateData(self):
        self.es.update(index="my_index", doc_type="test_type",
                       id=0, ignore=[400, 409], body={"doc": {"name": "python1", "addr": "上海"}})
        # 更新结果
        result = self.es.get(index="my_index", doc_type="test_type", id=1)
        print('\n数据id=11更新完成：\t', result['_source']['name'])

    def ParaSearch(self):
        query1 = self.es.search(index="my_index", body={"query": {"match_all": {}}})
        print('\n查询所有文档\n', query1)

        query2 = self.es.search(index="my_index", body={"query": {"term": {'name': 'python'}}})
        print('\n查找名字Python的文档:\n', query2['hits']['hits'][0])


if __name__ == '__main__':
    EsAction().ParaSearch()
