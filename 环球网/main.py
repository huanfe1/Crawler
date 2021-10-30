# _*_ coding:utf-8 _*_

"""
时间:2021年10月27日
作者:幻非
"""
import re
import get
import requests

url = 'https://opinion.huanqiu.com/article/45LrB3bSYU4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 '
}
# get.data_edit(url)


def get_html(self):
    response = requests.get(url=self, headers=headers).text
    html = re.findall('<li><a href="//(.*?)"', response)
    html0 = []
    for ss in html:
        if ss.find('gallery') == -1:
            ss = 'https://' + ss
            html0.append(ss)
    html.clear()
    html = html + html0
    # print(len(html))
    return html


get_all = get_html(url)
a = 0
while len(get_all) <= 10:
    get_all = get_all + get_html(get_all[a])
    a = a + 1
for i in get_all:
    get.data_edit(i)


