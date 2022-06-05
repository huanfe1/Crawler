# _*_ coding:utf-8 _*_

import requests
import time

AUTHOR_ID = 'MS4wLjABAAAAtRfhWq2zu4zwVCVkIowOm3cGO4WyIHiURAW5ROo1SnY'

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    'Referer': 'https://www.douyin.com/',
}


def craw(max_cursor=0):
    url = f'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid={AUTHOR_ID}&count=21&max_cursor={max_cursor}&_signature=yk5HowAAqENrJ2AQdlZniMpOR7'

    response = requests.get(url=url, headers=headers).json()

    if response['has_more']:
        video_list = []

        for aweme in response['aweme_list']:
            temp = [aweme['desc'], aweme['video']['play_addr']['url_list'][0]]
            video_list.append(temp)
        download(video_list)
        craw(response['max_cursor'])

    else:
        print("获取作品完毕")


def download(url_list: list):
    for tittle, url in url_list:
        print(tittle)
        with open(f'{tittle}.mp4', 'wb') as file:
            file.write(requests.get(url=url, headers=headers).content)
        time.sleep(0.5)


craw()
