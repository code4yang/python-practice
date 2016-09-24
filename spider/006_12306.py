import logging
import logging.config
import re

import requests
from prettytable import PrettyTable
from pymongo import MongoClient


def get_station_info(url=r'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8964'):
    """
    获取车站信息，包括中文名，拼音全拼，缩写等
    :param url:
    :return:
    """
    logger = logging.getLogger(__name__)
    logger.info('starting get station info')
    resp = requests.get(url=url, verify=False)
    reg = re.compile(r'@[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|[^\|]*\|[0-9]*')
    all = reg.findall(resp.text)
    logger.info(str(len(all)) + ' station infos has got')
    return all


def write2mongo(stations):
    """
    将车站信息写入到mongodb中
    :param stations: 车站信息，用 | 分隔统一车站的各个信息
    :return:
    """
    try:
        logger = logging.getLogger(__name__)
        logger.info('starting write station info')
        con = MongoClient('localhost', 27017)  # 连接mongodb
        data_list = []
        for station in stations:
            parts = ('' + station).split('|')
            data = {
                'Chinese': parts[1],
                'ext': parts[2],
                'pinyin': parts[3],
                'abbr': parts[4],
                'order': parts[5]
            }
            data_list.append(data)
        local = con.get_database('python')
        collection = local.get_collection('12306_station')
        collection.remove()  # clear data before insert ,in case duplicate
        collection.insert_many(data_list)
        con.close()
        logger.info('write {0} station info :　Done'.format(len(data_list)))
    except IOError as e:
        logger.error(e)


def get_ticket_info(date, from_station, to_station, purpose_code='ADULT'):
    logger = logging.getLogger(__name__)
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes={0}&queryDate={1}&from_station={2}&to_station={3}'
    url = url.format(purpose_code, date, from_station, to_station)
    logger.info('request url: ' + url)
    resp = requests.get(url=url, verify=False)
    tickets = resp.json()['data']['datas']
    return tickets


def display_info(tickets):
    table = PrettyTable()
    t_headers = (
        '车次', '始发站', '终到站', '出发站', '目的站', '日期', '发车时间', '到达时间', '历时', '隔天', '开售时间', '商务座', '特等座', '一等座', '二等座', '高级软卧',
        '软卧', '硬卧', '软座', '硬座', '无座', '其他', '网上购票')
    table.field_names = t_headers
    for ticket in tickets:
        row = (ticket['station_train_code'], ticket['start_station_name'], ticket['end_station_name'],
               ticket['from_station_name'], ticket['to_station_name'], ticket['start_train_date'], ticket['start_time'],
               ticket['arrive_time'], ticket['lishi'], ticket['day_difference'], ticket['sale_time'], ticket['swz_num'],
               ticket['tz_num'], ticket['zy_num'], ticket['ze_num'], ticket['gr_num'], ticket['rw_num'],
               ticket['yw_num'], ticket['rz_num'], ticket['yz_num'], ticket['wz_num'], ticket['qt_num'],
               ticket['canWebBuy'])
        table.add_row(row)
    print(table)


if __name__ == "__main__":
    logging.config.fileConfig("log.conf")
    requests.packages.urllib3.disable_warnings()
    # stations = get_station_info()
    # write2mongo(stations)
    tickets = get_ticket_info('2016-10-03', 'SSH', 'NCG')
    display_info(tickets)
