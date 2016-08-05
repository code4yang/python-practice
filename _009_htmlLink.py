"""
从一个html文件中获取所有的链接
"""
from bs4 import BeautifulSoup


def get_content_by_tag_name(filename, tag_name="a"):
    """
    通过文件名打开html文件，获取其中标签为tagname的内容并返回
    :param filename: html文件的文件名
    :param tag_name: 需要获取的标签名
    :return: 获取到的标签对象集
    """
    if not (filename.endswith('.html') or filename.endswith('.mhtml')):
        return None
    file = open(filename, encoding='utf-8')
    soup = BeautifulSoup(file.read(), 'lxml')
    return soup.find_all(name=tag_name)

links = get_content_by_tag_name('E:\personal\python\BeautifulSoup.mhtml', "a")
for link in links:
    print(link.get('href'))
