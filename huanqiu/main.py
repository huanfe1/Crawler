# _*_ coding:utf-8 _*_

"""
时间:2021年10月27日
作者:幻非
"""

import re
import string
import random
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 '
}

url = 'https://opinion.huanqiu.com/article/45KiJcfV0wT'

response = requests.get(url=url, headers=headers).text

get_data = re.findall('data-type="rtext"><p>(.*?)</p></section>', response)[0]


def getKey(self):
    data = string.ascii_letters + string.digits
    key = random.sample(data, self)
    keys = "".join(key)
    return keys


def data_edit(self):
    try:
        """尝试获取AD广告信息"""
        get_ad = '</p><aside id="content-ad"' + re.findall('</p><aside id="content-ad"(.*?)<p>', self)[0] + "<p>"
    except IndexError:
        pass
    else:
        self = self.replace(get_ad, '')

    try:
        """尝试获取文章配图信息"""
        get_pic = re.findall('<i class=(.*?)</i>', self)
        for i in get_pic:
            i = "<i class=" + i + "</i>"
            self = self.replace(i, '')
            # 这里的list是将元组转为列表
            pic_name = list(re.findall('data-alt="(.*?)" src="//(.*?)" /></i>', i)[0])
            if not pic_name[0]:
                pic_name[0] = str(getKey(8))
            pic_data = requests.get(url='https://' + pic_name[1], headers=headers).content
            with open(pic_name[0] + '.jpg', mode='wb') as file:
                file.write(pic_data)
    except IndexError:
        pass

    try:
        """换行"""
        self = self.replace("</p><p>", '\n')
        self = self.replace("\n\n", '\n')
        self = self.replace("\n\n\n", '\n')
    except IndexError:
        pass

    print(self)


data_edit(get_data)
