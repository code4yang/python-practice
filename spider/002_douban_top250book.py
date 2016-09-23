from bs4 import BeautifulSoup
import requests


def get_top250_book(books, url='http://book.douban.com/top250', flag=False):
    """
    get top 250 books from douban
    :param books:a list save book's title and info
    :param url: douban book index page
    :param flag: if it's True, it will find the next page
    :return: None
    """
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', attrs={'class': 'indent'})
    tds = content.find_all('td', attrs={'valign': 'top'})
    for td in tds:
        info = td.p
        if info is not None:
            title = td.div.a.attrs['title']
            books.append(title + '  ' + info.string)
    if flag:
        pager = content.find('div', attrs={'class': 'paginator'})
        next = pager.find('span', attrs={'class': 'next'})
        if next is not None and next.a is not None:
            get_top250_book(books, next.a.get('href'), flag)

if __name__ == '__main__':
    lists = []
    get_top250_book(lists, flag=True)
    count = 1
    file = open('top250Book.txt', 'wt')
    for item in lists:
        print(count, item)
        count += 1
        file.writelines(item + '\r\n')
