# _*_ coding:utf-8 _*_

"""
时间:2021年10月28日
作者:幻非
"""

import os
import random
import re
import string

import requests

try:
    os.mkdir('.\\resource')
except FileExistsError:
    pass


def data_edit(self):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.159 Safari/537.36 '
    }
    response = requests.get(url=self, headers=headers).text
    try:
        get_data = re.findall('data-type="rtext"><p>(.*?)</p></section>', response)[0]
    except IndexError:
        print("不可执行", self)
        pass
    else:
        try:
            """尝试获取并删除AD广告信息"""
            get_ad = '</p><aside id="content-ad"' + re.findall('</p><aside id="content-ad"(.*?)<p>', get_data)[0] + "<p>"
            get_data = get_data.replace(get_ad, '')
        except IndexError:
            pass

        try:
            """尝试获取删除文章配图信息并保存图片"""
            get_pic = re.findall('<i class=(.*?)</i>', get_data)
            for i in get_pic:
                i = "<i class=" + i + "</i>"
                get_data = get_data.replace(i, '')
                # # 这里的list是将元组转为列表,为保存图片做准备
                # pic_name = list(re.findall('data-alt="(.*?)" src="//(.*?)" /></i>', i)[0])
                # if not pic_name[0]:
                #     pic_name[0] = str(getKey(8))
                # pic_data = requests.get(url='https://' + pic_name[1], headers=headers).content
                # with open(pic_name[0] + '.jpg', mode='wb') as file:
                #     file.write(pic_data)
        except IndexError:
            pass

        try:
            """换行"""
            get_data = get_data.replace("</p><p>", '\n')
            get_data = get_data.replace("\n\n", '\n')
        except IndexError:
            pass

        # 获取文章标题
        if get_data.find('video') == -1 and get_data != '':
            tittle = re.findall('<title>(.*?)</title><script', response)[0]
            get_data = tittle + '\n' + get_data

            with open('resource\\' + tittle + '.txt', 'w', encoding='utf-8') as file:
                file.write(get_data)


def getKey(self):
    data = string.ascii_letters + string.digits
    key = random.sample(data, self)
    keys = "".join(key)
    return keys


if __name__ == "__main__":
    data_edit('https://mil.huanqiu.com/article/45LrhUux7TU')