import requests
r = requests.get('https://github.com/timeline.json')
print(r)
print(type(r))