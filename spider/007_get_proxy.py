"""
从xicidaili上获取代理信息
"""
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


def get_proxy(url=r"http://www.xicidaili.com/"):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}
    resp = requests.get(url, headers=header)
    soup = BeautifulSoup(resp.content, 'lxml')
    trs = soup.find_all(is_proxy_row)
    proxys = []
    for tr in trs:
        tds = tr.find_all('td')
        if len(tds) > 7:
            proxy = {
                'ip': tds[1].text,
                'port': tds[2].text,
                'addr': tds[3].text,
                'anonymous': tds[4].text,
                'type': tds[5].text,
                'aliveTime': tds[6].text,
                'verifyTime': tds[7].text
            }
            proxys.append(proxy)
    return proxys


def is_proxy_row(tag):
    clazz = tag.get('class')
    if not isinstance(clazz, list):
        return False
    if len(clazz) > 0 and (clazz[0] == '' or clazz[0] == 'odd'):
        return True
    return False


def main():
    proxys = get_proxy()
    with MongoClient(host='localhost', port=27017) as client:
        db = client.get_database('local')
        col = db.get_collection('proxys')
        col.remove()  # 保存数据之前先清除原来的数据，以保证数据库中数据的有效性
        col.insert_many(proxys)
        print('Fetch Successful!')

if __name__ == '__main__':
    main()
