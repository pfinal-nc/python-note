# -*- coding:utf-8 -*-

# match()
import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d+\s\d{4}\s\w{10}',content)
# print(result)
# print(result.group())
# print(result.span())

# 匹配目标

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld',content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())
# print('\n======================\n')
# result_t = re.match('^Hello.*Demo$', content)
# print(result_t)
#
# # 贪婪与非贪婪
# result_s = re.match('^He.*?(\d+).*Demo$',content)
# print(result_s.group())
# print(result_s.group(1))

# 修饰符
# content = ''' Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^(\s+)He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(2))

# search()
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result.group(1))
#
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
#         </li>
#     </ul>
# </div>'''
# result_t = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)
# print(result_t.group(1),result_t.group(2))
#
# result_s = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(result_s)
# for result_l in result_s:
#     print(result_l)

# sub()
# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d+','',content)
# print(content)

# compile()

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
