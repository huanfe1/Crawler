# _*_ coding:utf-8 _*_

"""
时间:2021年10月09日
作者:幻非
"""

import time
import requests
import re
import os

url = 'http://jandan.net/top-4h'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 '
}

if not os.path.exists("resources"):
    os.mkdir("resources")

result = requests.get(url=url, headers=headers).text
tabs = re.findall('<a href="(.*?)">(.*?)</a></div>', result)
for i in tabs:
    hot_tabs = os.path.dirname(url) + i[0]
    result = requests.get(url=hot_tabs, headers=headers).text
    pic = re.findall('<p><a href="//(.*?)" target="_blank" class="view_img_link"', result)
    for self in pic:
        pic_data = requests.get(url='https://' + self, headers=headers).content
        with open('resources' + '\\' + os.path.basename(self), mode='wb') as file:
            file.write(pic_data)
        print('https://' + self)
        time.sleep(0.2)
