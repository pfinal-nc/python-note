# requests
import requests
import re
r = requests.get('https://www.douban.com/time/?dt_time_source=douban-web_anonymous')
print(r.status_code)

# string = re.findall(r'<img src=".*" alt=".*" class="avator">',r.text)
# print(string);
print(r.url)
print(r.encoding)
print(r.json)
