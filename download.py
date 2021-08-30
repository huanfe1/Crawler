# -*- coding:utf-8 -*-

"""
时间:2021年08月30日
作者:幻非
"""

import requests
import re

url = "https://www.douyin.com/video/6989540944248884517"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 '
}

# 获取网页源码
response = requests.get(url=url, headers=headers)
html_data = re.findall('src(.*?)vr%3D%22', response.text)[1]
video_url = requests.utils.unquote(html_data).replace('":"//', 'http://')  # url解码
print(video_url)

# 参照视频：https://www.bilibili.com/video/BV1tA411c7Vg
