# _*_ coding:utf-8 _*_
import time

import requests
import re
import os


def craw(url):
    headers = {
        'report-to': '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=1xeiHp1dw0L706DFWLaJyIKHH6w72FYcq9KoygxwGbpbEMvHbVRtXwlDYrjFMHholbYXiQV32pu9iXXPXfDcClAWWOBuNpOn2%2FboKTbD9NZ070tu4aHH8X8e5GX%2FjYK0aTuovTiqOh9F46rjuA%3D%3D"}],"group":"cf-nel","max_age":604800}',
        'nel': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}',
        'Connection': 'close'
    }
    list_url = re.findall('<a href="(.*?)"><i class="icon-list">', requests.get(url).text)[0]
    response = requests.get(list_url).text
    pics = re.findall('<img src="/style/logo/jz.png" lazysrc=(.*?) >', response, re.S)
    tittle = re.findall('<meta name="description" content="(.*?)\r\n', response)[0]
    print(tittle)
    if not os.path.exists(f'resources\\{tittle}'):
        os.mkdir(f'resources\\{tittle}')
    for i in pics:
        pic_url = i.replace('\r\n', '')
        pic_name = pic_url.split('/')[-1]
        print(pic_url)
        print(requests.get(pic_url, headers=headers))
        # with open(f'resources\\{tittle}\\{pic_name}', 'wb') as file:
        #     file.write(requests.get(pic_url).content)
        break
        time.sleep(2)


if __name__ == '__main__':
    craw('https://www.192tp.com/gq/imiss/im658.html')
