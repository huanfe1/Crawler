# _*_ coding:utf-8 _*_

import csv
import re

import requests

f = open('resource/music.csv', 'w', newline='', encoding='utf-8')
csv_write = csv.writer(f)
csv_write.writerow(['排名', '名称', '作者', '年份', '类型', '评分'])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


def craw(url, page):
    response = requests.get(url=url, headers=headers).text
    get_data = re.findall('<a class="nbg" href=.*?onclick="moreurl(.*?)".*?'
                          'title="(.*?)".*?'
                          '<p class="pl">(.*?)</p>.*?'
                          '<span class="rating_nums">(.*?)</span>.*?', response, re.S)
    for num, i in enumerate(get_data):
        i = list(i)
        i[0] = str(num + page + 1)
        i[1] = i[1].split('-')[-1].strip()
        author = i[2].split('/')[0]
        year = i[2].split('/')[1].strip()
        style = i[2].split('/')[-1].strip()
        i.pop(2)
        i.insert(2, style)
        i.insert(2, year)
        i.insert(2, author)
        csv_write.writerow(i)
        print(i)


for j in range(0, 250, 25):
    craw(f'https://music.douban.com/top250?start={j}', j)
f.close()
