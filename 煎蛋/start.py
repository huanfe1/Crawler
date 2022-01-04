# _*_ coding:utf-8 _*_

"""
时间:2021年10月09日
作者:幻非
"""

import os
import re
import threading
import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 '
}

if not os.path.exists("resources"):
    os.mkdir("resources")


def save_pic(pic_url):
    print(pic_url)
    time.sleep(2)
    pic_data = requests.get(url='https://' + pic_url, headers=headers).content
    with open('resources' + '\\' + os.path.basename(pic_url), 'wb') as f:
        f.write(pic_data)


def get_pic(html_url):
    time.sleep(2)
    result = requests.get(url=html_url, headers=headers).text
    pic = re.findall('<p><a href="//(.*?)" target="_blank" class="view_img_link"', result)
    threads = []
    for self in pic:
        threads.append(
            threading.Thread(target=save_pic, args=(self,))
        )

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


urls = [
    "http://jandan.net/top-tucao",
    "http://jandan.net/top-tucao",
    "http://jandan.net/top",
    "http://jandan.net/top-ooxx",
    "http://jandan.net/top-zoo",
    "http://jandan.net/top-3days"
]

pic_threads = []
for i in urls:
    pic_threads.append(
        threading.Thread(target=get_pic, args=(i, ))
    )

for pic_thread in pic_threads:
    pic_thread.start()
for pic_thread in pic_threads:
    pic_thread.join()
