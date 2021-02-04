import requests

r = requests.get('https://www.google.com')
print(r)
print(r.text)
print(r.content)
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.encoding)
print(r.history)
r.close()
