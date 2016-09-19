"""
网站http://www.nruan.com/win-key.html内有回复百度盘链接
先拿到链接及密码，再访问百度网盘下载网页信息
"""
import re

import requests
from bs4 import BeautifulSoup


def get_file_link(url=r'http://www.nruan.com/win-key.html'):
    resp = requests.get(url=url)
    soup = BeautifulSoup(resp.content, 'lxml')
    wows = soup.find_all(text=re.compile(r'http://pan.baidu.com'))
    print(wows)


if __name__ == '__main__':
    get_file_link()
