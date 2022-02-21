# _*_ coding:utf-8 _*_

"""
时间:2021年10月30日
作者:幻非
"""

import os
import re
import time

import requests
from bs4 import BeautifulSoup


def chapter(chapter_url):
    """保存章节内容"""
    response = requests.get(url=chapter_url).text
    soup = BeautifulSoup(response, 'html.parser')
    novel_tittle = re.findall('(.*?)_', soup.find('title').string)[0]
    content = soup.find('div', itemprop="acticleBody").find_all('p')
    tittle = soup.find('div', {'class': "title_txtbox"})
    content0 = []
    for i in content:
        content0.append(i.string)
    content = str(tittle.string) + '\n' + '\n'.join(content0)
    with open(novel_tittle + '//' + str(tittle.string) + '.txt', 'w', encoding='utf-8') as file:
        file.write(content)


def chapter_list(_self):
    """获取所有章节链接,并将作者信息保存"""
    if _self.find('com/book') != -1:
        _self = _self.replace('com/book', 'com/showchapter')
    response = requests.get(url=_self).text
    soup = BeautifulSoup(response, 'html.parser').find('div', {'class': 'book-meta'})
    tittle = soup.find('h1').string
    # 作者信息
    writer_info = f"作者:{str(soup.find('a').string)}  主页地址:{str(soup.find('a')['href'])}"
    # 更新信息
    update = soup.find_all('span')[1].get_text() + '\n' + soup.find_all('span')[2].get_text()
    # 信息汇总
    info = tittle + '\n' + writer_info + '\n' + update
    if not os.path.exists(tittle):
        os.mkdir(tittle)
    with open(tittle + "//" + "作者信息" + '.txt', "w", encoding='utf-8') as file:
        file.write(info)
    soup = BeautifulSoup(response, 'html.parser').find('div', {'class': 'volume-list'}).find_all('li')
    chapter_link = []
    for i in soup:
        # 去除VIP文章
        if str(i).find('vip') == -1:
            chapter_link.append(re.findall('href="(.*?)"', str(i))[0])
        else:
            print("接下来的内容需要VIP才能观看哦")
            break
    return chapter_link


if __name__ == "__main__":
    url = 'http://book.zongheng.com/showchapter/672340.html'
    for i in chapter_list(url):
        print(i)
        chapter(i)
        time.sleep(1)
