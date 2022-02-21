# _*_ coding:utf-8 _*_

import re
import threading
import requests

urls = [f'https://desk.3gbizhi.com/deskMV/index_{i}.html' for i in range(1, 22)]

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}


def get_pic_url(url):
    """获取图片网址"""
    pic_save_threads = []
    response = requests.get(url=url).text
    pic_url = re.findall('lazysrc2x="(.*?).556.308.jpg 2x" alt="(.*?)" ', response)
    for i in pic_url:
        pic_save_threads.append(
            threading.Thread(target=save_pic, args=(i,))
        )
    for i in pic_save_threads:
        i.start()


def save_pic(url_tittle):
    """保存图片"""
    pic_url, tittle = url_tittle
    print(tittle)
    pic_data = requests.get(url=pic_url).content
    with open('resources\\' + tittle + '.jpg', 'wb') as file:
        file.write(pic_data)


for i in urls:
    threads = [threading.Thread(target=get_pic_url, args=(i,))]
    for j in threads:
        j.start()
    for j in threads:
        j.join()