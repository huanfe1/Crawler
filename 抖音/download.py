# -*- coding:utf-8 -*-

"""
时间:2021年08月30日
作者:幻非
"""

import requests
import re
import os


def download(url):
    filename = "video\\"
    if not os.path.exists(filename):
        os.mkdir(filename)

    headers = {
        'cookie': 'MONITOR_WEB_ID=af96e502-3ab7-431c-8fc1-a7f9f8b90919; MONITOR_DEVICE_ID=31f46af8-a333-4c30-a2ec-85f974d96a73; douyin.com; __ac_nonce=061f5620a00cc87ee9cb3; __ac_signature=_02B4Z6wo00f01Ogj52gAAIDBw6m8r8D5pzjoA-PAAFwD2e; ttcid=12364d437d1742feaa9563e47e1a61a360; ttwid=1|_aMpRxbhOwdaCkmxSYRXqbDTYJ2TsSFtafupQTc2XPM|1643471370|28e7f25feb1ffe4e41fdf539ff67caec96acc3155937e451467748d24764c37c; _tea_utm_cache_6383=undefined; home_can_add_dy_2_desktop=0; AB_LOGIN_GUIDE_TIMESTAMP=1643471369920; _tea_utm_cache_1300=undefined; MONITOR_WEB_ID=7b442485-5a31-4dee-b3a9-f05b5156d402; s_v_web_id=verify_kz00f5m0_SmPWOiYI_yTOT_4oGR_8JyI_XnHM8RKMY6Mw; passport_csrf_token_default=02644b09634ab771d296f08c0aaacb39; passport_csrf_token=02644b09634ab771d296f08c0aaacb39; msToken=uYs6DpheNDuCCA6roxlTxCi3WHygiCWcBN2Hb9U7yw6g4hHiHHH07xPVVpnbUdDyjaJj01opH3cY36eBjOCoxuiR8Qdba0ljh4fASUmpKFxxBUE=; msToken=T6xyv3TmAzQHloNYyggABqYs0-mF4HKhhjlFhTEABJg3BGT6ek6wkBEZWjzeeHvGTB-MW30PJAXIgS9t5AztNnSStu3894fkry1r8lx5lwmPBfM44cFwBzxCc1Pe-IBEaA==; THEME_STAY_TIME=6001',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers).text.encode('GBK', 'ignore').decode('GBK')

    html_data = re.findall('src(.*?)vr%3D%22', response)[1]
    # 解码处理
    video_url = requests.utils.unquote(html_data).replace('":"//', 'http://')

    title = re.findall('<title data-react-helmet="true">(.*?)</title>', response)[0]

    video_content = requests.get(url=video_url, headers=headers).content

    with open(filename + title + '.mp4', mode='wb') as f:
        f.write(video_content)


if __name__ == '__main__':
    download("https://www.douyin.com/video/7058229415322438920")

"""
参考资料:
https://www.bilibili.com/video/BV1tA411c7Vg
"""
