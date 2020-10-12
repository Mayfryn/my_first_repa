import requests

# r = requests.get('https://api.github.com/events')
# print(r)
#
url = 'https://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}
req = requests.get(url, headers=headers)
print(req.text)

# r = requests.get("http://wikipedia.org")
# print(r)
# print(type(r))
# print(r.status_code)
# print(r.headers)
# print(r.request.headers)
# print(r.url)