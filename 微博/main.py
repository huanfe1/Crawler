# _*_ coding:utf-8 _*_

import os
import random
import time
import urllib.parse

import requests


def craw(url) -> list:
    """抓取网页内视频跟图片"""
    resources = []
    response = requests.get(url).json()
    if response['ok'] == 0:
        return []
    for card in response['data']['cards']:
        if 'pics' in card['mblog']:
            for pic in card['mblog']['pics']:
                resources.append(pic['large']['url'])
        # 如果不希望爬取视频，则注释到下面的两行
        if 'live_photo' in card['mblog']:
            resources.extend(card['mblog']['live_photo'])
    return resources


def download(url, author):
    """将资源下载到本地"""
    if 'media' in url:
        # url解码
        url = urllib.parse.unquote(url)
    name = url.split('/')[-1]
    with open(f'resources\\{author}\\{name}', 'wb') as file:
        file.write(requests.get(url).content)


def main():
    # 作者ID
    containerid = 2837256310
    page = 3
    author_url = f'https://m.weibo.cn/api/container/getIndex?type=uid&value={containerid}&containerid=100505{containerid}'
    author_name = requests.get(author_url).json()['data']['userInfo']['screen_name']
    check_file(f'resources\\{author_name}')
    while True:
        url = f'https://m.weibo.cn/api/container/getIndex?containerid=107603{containerid}_-_WEIBO_SECOND_PROFILE_WEIBO&page={page}'
        res = craw(url)
        if not res:
            print('抓取结束')
            break

        for i in res:
            print(i)
            time.sleep(random.random())
            download(i, author_name)
        time.sleep(random.randint(1, 3))
        page += 1


def check_file(path):
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':
    check_file('resources')
    main()
