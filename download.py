# -*- coding:utf-8 -*-

"""
时间:2021年08月30日
作者:幻非
"""

import requests
import re
import os


# 下载获取到的视频页地址中的视频
def download(url):
    # 判断是否该有该目录，如果没有则创建
    filename = "video\\"
    if not os.path.exists(filename):
        os.mkdir(filename)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.159 Safari/537.36 '
    }
    # 获取视频页源码
    response = requests.get(url=url, headers=headers)
    # 从视频页源码中获取大概视频地址
    html_data = re.findall('src(.*?)vr%3D%22', response.text)[1]
    # 解码大概视频地址获取视频具体地址
    video_url = requests.utils.unquote(html_data).replace('":"//', 'http://')
    # 获取视频标题
    title = re.findall('><title data-react-helmet="true">(.*?)</title>', response.text)[0]
    # 将视频处理为代码
    video_content = requests.get(url=video_url, headers=headers).content
    # 将代码保存
    with open(filename + title + '.mp4', mode='wb') as f:
        f.write(video_content)


# 如果作为模块被调用时不执行
if __name__ == '__main__':
    download("https://www.douyin.com/video/7002147170879081741")

"""
参考资料:
https://www.bilibili.com/video/BV1tA411c7Vg
"""
