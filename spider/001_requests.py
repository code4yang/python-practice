import requests
from bs4 import BeautifulSoup
"""
抓取zdfans首页所有程序列表
"""

resp = requests.get(r'http://www.zdfans.com')
html = resp.text
soup = BeautifulSoup(html, 'lxml')
ul = soup.find('ul', attrs={'class': 'excerpt'})
li_list = ul.find_all('li')
for li in li_list:
    a = li.h2.a
    info = li.div.span
    print(a.attrs['title'], '  ', info.text)
