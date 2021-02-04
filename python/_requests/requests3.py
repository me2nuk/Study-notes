import requests

r = requests.get('https://www.google.com', headers = {'header_name':'header_value', 'header_name2':'header_value2'}, cookies={'Cookie1':'Cookie_value', 'Cookie2':'Cookie_value2'})
print(r)

r = requests.get('https://www.google.com', data = {'date1':'date_value'})
print(r)

r = requests.get('https://www.google.com', timeout=2)
print(r)