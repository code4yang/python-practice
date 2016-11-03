#!/usr/bin/env python
"""
按照第二列名字将第一列数据分组并用','组合
"""
def parse():
    file = open('list.txt', 'rt', encoding='utf-8')
    lines = file.readlines()
    results = {}
    lastFlag = ''
    nums = []
    for line in lines:
        line = line[:-1]
        parts = line.split(' 	')
        if lastFlag != parts[1]:
            if lastFlag != '':
                results.update({lastFlag: nums})
            lastFlag = parts[1]
            nums = []
        nums.append(parts[0])
    for k, v in results.items():
        print(k + ':' + ','.join(v))


if __name__ == '__main__':
    parse()
