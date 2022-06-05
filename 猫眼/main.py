# _*_ coding:utf-8 _*_

import requests
import execjs

base_url = 'https://www.maoyan.com/board/4'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

with open('maoyan.js', 'r', encoding='utf-8') as file:
    js_code = file.read()

params = execjs.compile(js_code).call('getParams')

url_params = '&'.join([key + '=' + str(value) for key, value in params.items()])

url = base_url + '?' + url_params
response = requests.get(url=url, headers=headers, params=params)

print(response.text)
