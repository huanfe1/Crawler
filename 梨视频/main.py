# _*_ coding:utf-8 _*_

import os
import re

import requests

try:
    os.mkdir('resources')
except FileExistsError:
    pass


def craw(url):
    video_id = url.split('_')[-1]
    videoStatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={video_id}&mrd=0.506835970061889'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Referer': url
    }

    response = requests.get(url=videoStatus, headers=headers)
    get_Data = response.json()
    systemTime = get_Data['systemTime']
    srcUrl = get_Data['videoInfo']['videos']['srcUrl']
    video_url = srcUrl.replace(systemTime, f'cont-{video_id}')
    video_name = re.findall('video.pearvideo.com">.*?<img class="img" src=".*?" alt="(.*?)">', requests.get(url).text, re.S)[0]
    with open(f'resources\\{video_name}.mp4', 'wb') as file:
        file.write(requests.get(video_url).content)


craw('https://www.pearvideo.com/video_1752857')
