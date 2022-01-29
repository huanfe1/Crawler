# -*- coding:utf-8 -*-

import requests
import re
import csv

f = open('data.csv', 'w', newline='', encoding='utf-8')
csv_write = csv.writer(f)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


def craw(url):
    response = requests.get(url=url, headers=headers).text
    get_data = re.findall(r'<li>.*?<div class="item">.*? <em class="">(.*?)</em>.*?<span class="title">(.*?)'
                          r'</span>.*?<p class="">.*?<br>(.*?)&nbsp', response, re.S)
    for i in get_data:
        i = list(i)
        i[2] = re.findall(r'\d+', i[2])[0]
        print(i)
        csv_write.writerow(i)


for i in range(0, 250, 25):
    craw(f'https://movie.douban.com/top250?start={i}')
f.close()
