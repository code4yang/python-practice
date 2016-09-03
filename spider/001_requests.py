import requests
from bs4 import BeautifulSoup
"""
抓取zdfans首页所有程序列表
"""
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}
resp = requests.get(r'http://www.zdfans.com',headers=header)
html = resp.content
soup = BeautifulSoup(html, 'lxml')
ul = soup.find('ul', attrs={'class': 'excerpt'})
li_list = ul.find_all('li')
for li in li_list:
    a = li.h2.a
    info = li.div.span
    print(a.attrs['title'], '  ', info.text)
