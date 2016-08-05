"""
获取html文件的正文，p标签内容
"""
from bs4 import BeautifulSoup


def get_p_tag_content(filename):
    """
    通过文件名打开html文件，获取其中p标签的内容并返回
    :param filename: html文件的文件名
    :return:
    """
    if not (filename.endswith('.html') or filename.endswith('.mhtml')):
        return None
    file = open(filename, encoding='utf-8')
    soup = BeautifulSoup(file.read(), 'lxml')
    content = []
    ps = soup.find(name='p')

    for p in soup.find_all(name='p'):
        content.append(p.content)
    return content


content = get_p_tag_content('E:\personal\python\BeautifulSoup.mhtml')
print(content)
