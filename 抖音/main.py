import os
import requests
import time
import threading

# 目标主页ID
AUTHOR_ID = 'MS4wLjABAAAAEEiNqraukfE48MLpRq7KmFAOgUNnwKknGSLK9ei3yHs'
# 爬取主页视频还是喜欢列表  post or like
TYPE = "post"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    'Referer': 'https://www.douyin.com/',
}


def craw(num=0, limit=10):
    """
    爬取视频
    :param num: 不建议进行修改
    :param limit: 抓取API次数
    :return:
    """
    if limit == 0:
        return
    url = f'https://m.douyin.com/web/api/v2/aweme/{TYPE}/?reflow_source=reflow_page&sec_uid={AUTHOR_ID}&count=21&max_cursor={num}'
    response = requests.get(url=url, headers=headers).json()
    urls = []
    if not response["aweme_list"]:
        print("视频爬取完成")
        return
    for i in response["aweme_list"]:
        urls.append([i['desc'], i['video']['play_addr']['url_list'][0]])
    threading.Thread(target=download, args=(urls,)).start()
    limit -= 1
    craw(response['max_cursor'], limit)


def download(url_list: list):
    for tittle, url in url_list:
        tittle = tittle.replace(" ", "")
        file_name = f'resources\\{tittle}.mp4'
        if os.path.exists(file_name):
            continue
        print(tittle)
        try:
            with open(file_name, 'wb') as file:
                file.write(requests.get(url=url, headers=headers).content)
        except OSError:
            pass
        time.sleep(0.5)


craw()
