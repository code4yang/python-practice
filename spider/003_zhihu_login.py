import requests
from bs4 import BeautifulSoup


def login_zhihu():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}
    session = requests.Session()
    resp = session.get('http://www.zhihu.com/#signin', headers=header)
    xsrf = BeautifulSoup(resp.content, 'lxml').find('input', attrs={'name': '_xsrf'}).attrs['value']
    data = {'_xsrf': xsrf, 'password': '1234560.', 'captcha_type': 'cn', 'remember_me': 'true',
            'email': '704298867@qq.com'}
    print(data)
    resp = session.post('http://www.zhihu.com/login/email', data=data, headers=header)
    print(resp.json())
    resp = session.get('http://www.zhihu.com/', headers=header)
    soup = BeautifulSoup(resp.content, 'lxml')
    print(soup)
    print(soup.find_all('h2', attrs={'class': 'feed-title'}))


login_zhihu()
