"""
统计英文文本中每个单词出现的次数。
使用正则表达式，re模块
"""
import re


def count_word(filename):
    """
    统计每个单词出现的次数
    :param filename: 文件名
    :return data:统计的结果dict
    """
    #  以utf-8格式打开文件
    file = open(filename, 'r', encoding='utf-8')
    if file is None:
        return   # 如果文件打开失败，直接返回
    line = file.read().lower()  # 读取文件中所有文本
    regex = re.compile(r'\b\w+\b')  # 得到正则，匹配两端含有单词边界的字符
    finds = regex.findall(line)  # 拿到所有匹配的字符串
    data = {}  # 新建空的dict，以便存放单词和统计数
    for find in finds:
        find = find.strip()  # 将单词两端的空白删除
        if find in data:
            data.update({find: data[find] + 1})  # 如果已存在于dict中，则更新该条数据，并将value+1
        else:
            data.update({find: 1})  # 如果该数据不存在于dict中， 则新建该数据，并将value赋值为1
    return data


count = count_word('englishStory.txt')
for (k, v) in count.items():
    print(k, ' : ', v)
