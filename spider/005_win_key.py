"""
网站http://www.nruan.com/win-key.html内有回复百度盘链接
先拿到链接及密码，再访问百度网盘下载网页信息
"""
import re

import bs4
import requests
from bs4 import BeautifulSoup


def get_file_link(url=r'http://www.nruan.com/win-key.html'):
    """

    :param url: 根据url搜索其中第一条百度盘的链接
    :return:
    """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}
    resp = requests.get(url=url,headers=header)
    soup = BeautifulSoup(resp.content, 'lxml')
    wows = soup.find_all(name='strong',text=re.compile('\W*福利666\W*'))
    print(wows[0].parent())


if __name__ == '__main__':
    get_file_link()
