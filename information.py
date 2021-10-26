# -*- coding:utf-8 -*-

"""
时间:2021年08月31日
作者:幻非
"""

import requests
import re


def information(self):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.159 Safari/537.36 '
    }

    response = requests.post(url=self, headers=headers).text

    html_data = re.findall('content="(.*?)"/><meta data-react-helmet=', response)
    get_inf = re.findall("(.*?)：(.*?)TA的抖音号是(.*?)，已有(.*?)个粉丝，收获了(.*?)个喜欢", html_data[1])[0]
    text = f"TA的抖音ID为：{get_inf[0]}，抖音号是42984577{get_inf[2]}，已有{get_inf[3]}个粉丝，收获了{get_inf[4]}个喜欢"
    print(text)


if __name__ == '__main__':
    url = "https://www.douyin.com/user/MS4wLjABAAAAMRu1bNLgJf95web7lF6M5yFxBVD2NYhriO3XVlKZj0k"
    information(url)
