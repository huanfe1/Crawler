# _*_ coding:utf-8 _*_
import os
import random
import re
import time
from threading import Thread

import bs4
import requests

try:
    os.mkdir('resources')
except FileExistsError:
    pass


def craw(li):
    img_id = re.findall('data-wallpaper-id="(.*?)"', str(li))[0]
    if '<span class="png">' in str(li):
        img_type = 'png'
    else:
        img_type = 'jpg'
    img_url = f'https://w.wallhaven.cc/full/{img_id[:2]}/wallhaven-{img_id}.{img_type}'
    print(img_url)
    with open(f'resources\\{img_id}.{img_type}', 'wb') as file:
        file.write(requests.get(url=img_url).content)
    time.sleep(random.randint(1, 3))


def main(url):
    response = requests.get(url).text
    soup = bs4.BeautifulSoup(response, features="html.parser")
    lis = soup.find('section', attrs={'class': 'thumb-listing-page'}).find_all('li')
    for li in lis:
        Thread(target=craw, args=(li,)).start()


main('https://wallhaven.cc/toplist?page=2')
