# _*_ coding:utf-8 _*_

import os
import random
import time
import urllib.parse

import requests


def craw(url):
    """抓取网页内视频跟图片"""
    resources = []
    response = requests.get(url).json()
    if response['ok'] == 0:
        return None
    for card in response['data']['cards']:
        if 'pics' in card['mblog']:
            for pic in card['mblog']['pics']:
                resources.append(pic['large']['url'])
        # 如果不希望爬取视频，则注释到下面的两行
        if 'live_photo' in card['mblog']:
            resources.extend(card['mblog']['live_photo'])
    return resources


def download(url):
    """将资源下载到本地"""
    if 'media' in url:
        # url解码
        url = urllib.parse.unquote(url)
    name = url.split('/')[-1]
    with open(f'resources\\{name}', 'wb') as file:
        file.write(requests.get(url).content)


def main():
    # 作者ID
    containerid = 2837256310
    page = 1
    while True:
        url = f'https://m.weibo.cn/api/container/getIndex?containerid=107603{containerid}_-_WEIBO_SECOND_PROFILE_WEIBO&page={page}'
        res = craw(url)
        if not res:
            print('抓取结束')
            break
        else:
            print(url)
            for i in res:
                print(i)
                time.sleep(random.random())
                download(i)
        time.sleep(random.randint(1, 3))
        page += 1


if __name__ == '__main__':
    if not os.path.exists('resources'):
        os.mkdir('resources')
    main()
