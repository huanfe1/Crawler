# _*_ coding:utf-8 _*_

"""
时间:2021年11月28日
作者:幻非
"""

import re
import threading
import requests
import os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

if not os.path.exists('resources'):
    os.mkdir('resources')


def save_pic(url, tittle):
    response = requests.get(url=url, headers=headers).content
    with open(f'resources\\{tittle}.jpg', 'wb') as f:
        f.write(response)
    print(url)


def craw(url):
    response = requests.get(url=url, headers=headers).text.encode('GBK', 'ignore').decode('GBK')
    get_data = re.findall('lazysrc2x="(.*?).556.308.jpg 2x" alt="(.*?)" title="', response)
    for i in get_data:
        threading.Thread(target=save_pic, args=(i[0], i[1])).start()


for i in range(1, 24):
    craw(f'https://desk.3gbizhi.com/deskMV/index_{i}.html')
