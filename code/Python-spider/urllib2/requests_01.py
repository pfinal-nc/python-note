import requests
# r = requests.get('https://github.com/timeline.json')
# print(r)
# print(type(r))

# r1 = requests.get('http://httpbin.org/get')
# print(r1.text)

data = {
    'name':'nc',
    'age':22
}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)