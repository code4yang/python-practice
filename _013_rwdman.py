"""
 修改changelog为特定格式
"""
import re


def read_changelog(filename):
    file = open(filename,mode='r',encoding='utf-8')
    lines = file.readlines()
    reg = re.compile(r'\W*[AM]\W*(/.*\.\w*)$')
    rtn_list = []
    for line in lines:
        print(line)
        result = reg.match(line)
        if result is not None:
            rtn_list.append(result.group(1))
    return rtn_list

if __name__ == '__main__':
    rtnList = read_changelog('changeLog.txt')
    print(rtnList)
