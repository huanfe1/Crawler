# -*- coding:utf-8 -*-

"""
时间:2021年08月31日
作者:幻非
"""

from selenium import webdriver
import time

url = "https://www.douyin.com/user/MS4wLjABAAAAMRu1bNLgJf95web7lF6M5yFxBVD2NYhriO3XVlKZj0k"


def drop_down():
    """执行滚动操作"""
    for x in range(1, 100, 4):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


# 操作浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get(url)
# 给予等待时间滑动验证码
time.sleep(3)
# 往下滚动刷新出全部视频
drop_down()
# 获取视频地址
lis = driver.find_elements_by_css_selector('#root > div > div:nth-child(2) > div > '
                                           'div._67f6d320f692f9e5f19d66f4c8a1ecf9-scss > '
                                           'div._927ae3b0dd790b5b62eae61c7d2fa0bc-scss > div:nth-child(2) > ul li ')
for li in lis:
    li_url = li.find_element_by_css_selector('a').get_attribute('href')
    print(li_url)


"""
参考资料:
https://www.bilibili.com/video/BV1tA411c7Vg
"""
