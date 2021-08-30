# -*- coding:utf-8 -*-

"""
时间:2021年08月30日
作者:幻非
"""

import requests
import re
import os

filename = "video\\"
if not os.path.exists(filename):
    os.mkdir(filename)

url = "https://www.douyin.com/video/7002147170879081741"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 '
}

# 获取网页源码
response = requests.get(url=url, headers=headers)
html_data = re.findall('src(.*?)vr%3D%22', response.text)[1]  # 获取大概视频地址
title = re.findall('><title data-react-helmet="true">(.*?)</title>', response.text)[0]  # 获取视频标题
video_url = requests.utils.unquote(html_data).replace('":"//', 'http://')  # url解码
print(video_url)
video_content = requests.get(url=video_url, headers=headers).content

with open(filename + title + '.mp4', mode='wb') as f:
    f.write(video_content)


# 参照视频：https://www.bilibili.com/video/BV1tA411c7Vg
