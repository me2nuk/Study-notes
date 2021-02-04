import requests

GET = requests.get
POST = requests.post
PUT = requests.put
HEAD = requests.head
DELETE = requests.delete

print(GET('https://www.google.com').text)
print(POST('https://www.google.com').text)
print(PUT('https://www.google.com').text)
print(HEAD('https://www.google.com').text)
print(DELETE('https://www.google.com').text)