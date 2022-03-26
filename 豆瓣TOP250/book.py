# _*_ coding:utf-8 _*_

import csv
import re

import requests

f = open('resource/book.csv', 'w', newline='', encoding='utf-8')
csv_write = csv.writer(f)
csv_write.writerow(['排名', '名称', '评分', '作者', '年份', '评语'])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


def craw(url, page):
    response = requests.get(url=url, headers=headers).text
    get_data = re.findall('<a class="nbg" href=.*?onclick="moreurl(.*?)".*?'
                          'title="(.*?)".*?'
                          '<p class="pl">(.*?)</p>.*?'
                          '<span class="rating_nums">(.*?)</span>.*?'
                          '<span class="inq">(.*?)</span>', response, re.S)
    for i in get_data:
        i = list(i)
        i[0] = str(int(re.findall("i:'(.*?)'", i[0])[0]) + 1 + page)
        author = i[2].split('/')[0]
        year = i[2].split('/')[-2]
        i.pop(2)
        i.insert(3, year)
        i.insert(3, author)
        csv_write.writerow(i)
        print(i)


for i in range(0, 250, 25):
    craw(f'https://book.douban.com/top250?start={i}', i)
f.close()
