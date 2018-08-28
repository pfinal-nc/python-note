# -*- coding:utf-8 -*-
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
#result = etree.tostring(html)
#print(result.decode('utf-8'))

# 所有节点
# print(html.xpath('//*'))
# 获取所有li节点
result = html.xpath('//li')
# print(result)
# print(result[0])

# 子节点
result_c = html.xpath('//li/a')
result_c_all = html.xpath('//ul//a')
# print(result_c)
# print(result_c_all)

# 父节点
result_p = html.xpath('//a[@href="link4.html"]/../@class')
# print(result_p)
result_p_all = html.xpath('//a/parent::*/@class')
# print(result_p_all)

# 属性匹配
result_att = html.xpath('//li[@class="item-0"]')
# print(result_att)

# 文本获取
result_text = html.xpath('//li[@class="item-0"]/a/text()')
# print(result_text)

# 属性获取

result_attr = html.xpath('//li/@class')
# print(result_attr)

# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result_s = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result_s)

# 多属性匹配
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result_s = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result_s)

# 节点轴选择
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result_ht = html.xpath('//li[1]/ancestor::*')
print(result_ht)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)