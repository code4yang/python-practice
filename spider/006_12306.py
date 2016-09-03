import re

import requests
from pymongo import MongoClient


def get_station_info(url = r'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8964'):
    """
    获取车站信息，包括中文名，拼音全拼，缩写等
    :param url:
    :return:
    """
    resp = requests.get(url=url,verify=False)
    reg = re.compile(r'@[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|[0-9]*')
    all = reg.findall(resp.text)
    return all

def write2mongo(stations):
    """
    将车站信息写入到mongodb中
    :param stations: 车站信息，用 | 分隔统一车站的各个信息
    :return:
    """
    con = MongoClient('localhost', 27017)  # 连接mongodb
    dataList = []
    for station in stations:
        parts = (''+station).split('|')
        data={
            'Chinese':parts[1],
            'ext':parts[2],
            'pinyin':parts[3],
            'abbr':parts[4],
            'order':parts[5]
        }
        dataList.append(data)
    local = con.get_database('local')
    collection = local.get_collection('python12306')
    collection.insert_many(dataList)
    con.close()

if __name__=="__main__":
    stations = get_station_info()
    # write2mongo(stations)