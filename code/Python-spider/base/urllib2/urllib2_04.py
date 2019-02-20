# -*- coding:utf-8 -*-

# 解析链接
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import unquote
from urllib.parse import quote

result = urlparse('https://cn.bing.com/search?q=python&qs=n&form=QBLH&sp=-1&pq=python&sc=9-6&sk=&cvid=79E4E8C62F8D4711AB1A5BA47E3B2843')
print(type(result),result)
print(result.scheme,result[0],result.netloc,result[1],sep="\n")

# urlunparse()
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

# urlsplit()
results = urlsplit('https://cn.bing.com/search?q=python&qs=n&form=QBLH&sp=-1&pq=python&sc=9-6&sk=&cvid=79E4E8C62F8D4711AB1A5BA47E3B2843')
print(results)
print(results.scheme,result[0])

# urlunsplit() 与urlunparse()类似，它也是将链接各个部分组合成完整链接的方法，传入的参数也是一个可迭代对象，例如列表、元组等，唯一的区别是长度必须为5。
data_two = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data_two))

# urljoin()
print('\n===================\n')
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://cn.bing.com/FAQ.html'))

# urlencode()
params = {
    'name':'nc',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print("\n+++++\n" + url)

# parse_qs()
query = 'name=nc&age=22'
print(parse_qs(query))

# parse_qsl() parse_qsl()方法，它用于将参数转化为元组组成的列表，
query_t = 'name=nc&age=22'
print(parse_qsl(query_t))

# quote() 该方法可以将内容转化为URL编码的格式
keyword = '壁纸'
url_f = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url_f)

url_t = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url_t))

