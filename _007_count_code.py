"""
统计所有的代码行数。
TODO 需要添加对python代码中”“”三个引号注释的判断，问题在于字符串也会有三个引号的情况
"""
import os
import re


def count_code(filepath):
    """
    统计某个路径下所有.py文件的行数，注释行数（以#或三个"开头），空行行数
    :param filepath: py代码所在的文件夹路径
    :return:
    """
    dirs = os.listdir(filepath)
    for file in dirs:
        if file.endswith('.py'):
            count_file(file)


def count_file(filename):
    """
    统计某文件中含有的代码行数及注释行数
    :param filename:文件名
    :return:
    """
    file = open(filename, encoding='utf-8')  # 通过文件名打开文件
    regex = re.compile(r'^#')
    count = {'filename': filename, 'common': 0, 'code': 0, 'blank': 0}
    # flag = False  # 用于判断是否在“”“三个引号的注释中。若是，则设置为True
    for line in file:
        line = line.strip()
        # if line == r'"""':
        #     flag = not flag  # 取反，
        #     count.update({'common': count['common'] + 1})
        #     continue
        if regex.match(line):
            count.update({'common': count['common'] + 1})
        elif line == '':
            count.update({'blank': count['blank'] + 1})
        else:
            count.update({'code': count['code'] + 1})
    print(count)

count_code(os.path.abspath('.'))
