# _*_ coding:utf-8 _*_

"""
时间:2021年11月28日
作者:幻非
"""

import re
import time
import requests
import os

if not os.path.exists("resources"):
    os.mkdir("resources")
history_path = 'resources' + '\\' + 'history.txt'

if not os.path.exists(history_path):
    file = open(history_path, 'w')
    file.close()

with open(history_path, 'r', encoding="utf-8") as file:
    history = file.read()

save_pic_list = [i.replace('.jpg', '') for i in os.listdir('resources')]

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}


def grab(self):
    """抓取网页壁纸"""
    k = 0
    for j in range(5, 23):
        url = f'{self}index_{j}.html'
        if not history.count(url):
            print(url)
            url_source = requests.get(url=url, headers=headers).text
            url_state = requests.get(url=url, headers=headers).status_code
            if url_state == 200:
                get_tittle_list = re.findall(r'" alt="(.*?)" title="', url_source)
                for tittle in get_tittle_list:
                    if not save_pic_list.count(tittle):
                        include_pic_url = url_source[url_source.find(tittle) - 270:url_source.find(tittle) - 210]
                        pic_url = re.findall('href="(.*?)"', include_pic_url)[0]
                        pic_source = requests.get(url=pic_url, headers=headers).text
                        pic_path = re.findall('<a href="(.*?)" target="_blank" title=', pic_source)[0]
                        pic_content = requests.get(url=pic_path, headers=headers).content
                        with open('resources' + '\\' + tittle + '.jpg', 'wb')as f:
                            f.write(pic_content)
                        print(k, tittle, pic_url)
                        time.sleep(2)
                        k += 1
                with open(history_path, 'a', encoding="utf-8") as f:
                    f.write(url+'\n')
                time.sleep(2)
            elif url_state == 404:
                break


if __name__ == '__main__':
    grab("https://desk.3gbizhi.com/deskMX/")
