# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 15:01
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 布隆过滤器.py
# @Software: PyCharm
# 布隆过滤器 是一个二进制向量和一系列随机映射函数实现。 可以用于检索一个元素是否在一个集合中。
# 布隆过滤器应用场景
# 1. 数据库防止穿库
# 2. 业务场景中判断用户是否阅读过某视频或文章，比如抖音或头条，当然会导致一定的误判，但不会让用户看到重复的内容。
# 3. 缓存宕机、缓存击穿场景，一般判断用户是否在缓存中，如果在则直接返回结果，不在则查询db，如果来一波冷数据，会导致缓存大量击穿，造成雪崩效应，这时候可以用布隆过滤器当缓存的索引，只有在布隆过滤器中，才去查询缓存，如果没查询到，则穿透到db。如果不在布隆器中，则直接返回。
# 4. WEB拦截器，如果相同请求则拦截，防止重复被攻击。用户第一次请求，将请求参数放入布隆过滤器中，当第二次请求时，先判断请求参数是否被布隆过滤器命中。可以提高缓存命中率。
# 5. 大量爬虫数据去重
# 6. 保护数据安全：广告精确投放 ：广告主通过设备id，计算hash算法，在数据包（数据提供方）中去查找，如果在存在，则证明该设备id属于目标人群，进行投放广告，同时保证设备id不泄露。数据提供方和广告主都没有暴露自己拥有的设备id。

import mmh3 as mmh3
from bitarray import bitarray

BIT_SIZE = 5000000


class BloomFilter:
    """ bloom filter"""

    def __init__(self, bit_size=BIT_SIZE):
        # Initialize bloom filter, set size and all bits to 0
        self.bit_size = bit_size
        self.bit_array = bitarray(self.bit_size)
        self.bit_array.setall(0)

    def is_contain(self, url):
        # Check if a url is in a collection
        point_list = self.get_positions(url)
        is_contain = True
        for b in point_list:
            is_contain = is_contain and self.bit_array[b]
        return is_contain

    def get_positions(self, url):
        """ get positions"""
        return [mmh3.hash(url, 41 + i) % self.bit_size for i in range(7)]

    def add(self, url):
        """ add"""
        point_list = self.get_positions(url)
        for b in point_list:
            self.bit_array[b] = 1


if __name__ == '__main__':
    bl = BloomFilter()
    bl.add('baidu')
    result = bl.is_contain('baidu11')
    print(result)
