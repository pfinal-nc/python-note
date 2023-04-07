# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 17:50
# @Author  : PFinal南丞
# @Email   : lampxiezi@163.com
# @File    : search.py
# @Software: PyCharm
from elasticsearch7 import Elasticsearch

es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200}], timeout=3600)

query1 = es.search(index="lqz", body={"query": {"match_all": {}}})

print(query1)

query2 = es.search(index="lqz", body={"query": {"match_phrase_prefix": {'from': '广'}}})
print(query2)

query3 = es.search(index="lqz", body={"query": {"match_phrase": {"title": {"query": "中国世界", "slop": 2}}}})
print(query3)

query4 = es.search(index="lqz", body={"query": {"match": {"from": "gu"}}, "sort": [{"age": {"order": "asc"}}]})

print(query4)
