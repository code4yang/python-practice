# spider_test001---> http://www.zdfans.com
import urllib.request
import bs4
import re

try:
    url = 'http://www.zdfans.com'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8').__str__()
    soup = bs4.BeautifulSoup(content, 'lxml')
    ul = soup.select('.excerpt')
    lis = ul[0].contents
    pattern = re.compile('<h2><a.*? target="_blank".*?>(.*?)</a></h2>')
    for li in lis:
        print(li)
        m = pattern.match(li.__str__())
        print(m.group())
except Exception as e:
    print(e)
