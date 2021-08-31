# -*- coding:utf-8 -*-

"""
时间:2021年08月31日
作者:幻非
"""

import requests
import re


def information(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.159 Safari/537.36 '
    }

    response = requests.get(url=url, headers=headers)
    html_data = re.findall('<span><span><span><span>(.*?)</span></span></span>', response.text) + \
                re.findall('抖音号： <!-- -->(.*?)</p><p class=', response.text) + \
                re.findall("已有(.*?)个粉丝", response.text) + \
                re.findall("收获了(.*?)个喜欢，欢迎观看", response.text) + \
                re.findall('作品<span class="_03811320ee25b81d1c705fae532572ec-scss">(.*?)</span>', response.text)
    get_information = {"name": html_data[0], "ID": html_data[1], "fans": html_data[2], "like": html_data[3],
                       "work": html_data[4], }
    return get_information


if __name__ == '__main__':
    url = "https://www.douyin.com/user/MS4wLjABAAAAMRu1bNLgJf95web7lF6M5yFxBVD2NYhriO3XVlKZj0k"
    print(information(url))
